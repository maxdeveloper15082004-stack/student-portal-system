from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    advisor_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "role",
            "password",
            "register_number",
            "cgpa",
            "attendance",
            "std_class",
            "section",
            "advisor_name",
            "current_semester",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_advisor_name(self, obj):

        if obj.advisor_name:
            return obj.advisor_name

        if obj.role == User.STUDENT and obj.std_class and obj.section:

            matching_admin = User.objects.filter(
                role=User.ADMIN, std_class=obj.std_class, section=obj.section
            ).first()
            if matching_admin:
                return matching_admin.username
        return None

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "role",
            "register_number",
            "std_class",
            "section",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        role = validated_data.get("role", User.STUDENT)
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
            role=role,
            register_number=validated_data.get("register_number", ""),
            std_class=validated_data.get("std_class", ""),
            section=validated_data.get("section", ""),
        )
        return user
