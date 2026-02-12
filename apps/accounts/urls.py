from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    DashboardView,
    LogoutView,
    StudentUpdateView,
    AdminUpdateView,
    ForceLogoutView,
)
from django.views.generic import TemplateView

urlpatterns = [
    path("api/register/", RegisterView.as_view(), name="api_register"),
    path("api/login/", LoginView.as_view(), name="api_login"),
    path("api/logout/", LogoutView.as_view(), name="api_logout"),
    path("api/dashboard/", DashboardView.as_view(), name="api_dashboard"),
    path(
        "api/student/<int:pk>/update/",
        StudentUpdateView.as_view(),
        name="api_student_update",
    ),
    path("api/admin/update/", AdminUpdateView.as_view(), name="api_admin_update"),
    path(
        "api/student/<int:pk>/force-logout/",
        ForceLogoutView.as_view(),
        name="api_force_logout",
    ),
    path(
        "register/",
        TemplateView.as_view(template_name="register.html"),
        name="page_register",
    ),
    path("login/", TemplateView.as_view(template_name="login.html"), name="page_login"),
    path(
        "dashboard/",
        TemplateView.as_view(template_name="dashboard.html"),
        name="page_dashboard",
    ),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
]
