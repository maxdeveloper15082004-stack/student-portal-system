from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .serializers import RegisterSerializer, UserSerializer
from .models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response(UserSerializer(user).data)
        return Response(
            {"error": "Wrong credentials"}, status=status.HTTP_400_BAD_REQUEST
        )

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role == User.ADMIN:
            students = User.objects.filter(role=User.STUDENT).order_by(
                "register_number"
            )

            if user.std_class:
                students = students.filter(std_class=user.std_class)
            if user.section:
                students = students.filter(section=user.section)

            serializer = UserSerializer(students, many=True)
            user_serializer = UserSerializer(user)
            return Response(
                {
                    "role": "admin",
                    "data": serializer.data,
                    "profile": user_serializer.data,
                }
            )
        else:

            advisor_name = user.advisor_name
            current_semester = user.current_semester

            matching_admin = None
            if user.std_class and user.section:

                matching_admin = User.objects.filter(
                    role=User.ADMIN,
                    std_class__iexact=user.std_class,
                    section__iexact=user.section,
                ).first()

            if matching_admin:
                if not advisor_name:
                    advisor_name = matching_admin.username

                if matching_admin.current_semester:
                    current_semester = matching_admin.current_semester

            serializer = UserSerializer(user)
            data = dict(serializer.data)
            data["advisor_name"] = advisor_name
            data["current_semester"] = current_semester

            return Response({"role": "student", "data": data})

class StudentUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):

        if request.user.role != User.ADMIN:
            return Response(
                {"error": "Only admins can update student details."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

class AdminUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        if request.user.role != User.ADMIN:
            return Response(
                {"error": "Only admins can update their profile."},
                status=status.HTTP_403_FORBIDDEN,
            )

        response = super().update(request, *args, **kwargs)

        admin_user = self.get_object()

        admin_user.refresh_from_db()

        if admin_user.std_class and admin_user.section and admin_user.current_semester:

            User.objects.filter(
                role=User.STUDENT,
                std_class__iexact=admin_user.std_class,
                section__iexact=admin_user.section,
            ).update(current_semester=admin_user.current_semester)

        return response