from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = "admin"
    STUDENT = "student"

    ROLE_CHOICES = (
        (ADMIN, "Admin"),
        (STUDENT, "Student"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=STUDENT)
    register_number = models.CharField(max_length=20, blank=True, null=True)
    cgpa = models.FloatField(blank=True, null=True)
    attendance = models.FloatField(blank=True, null=True)
    std_class = models.CharField(max_length=20, blank=True, null=True)
    section = models.CharField(max_length=10, blank=True, null=True)
    advisor_name = models.CharField(max_length=100, blank=True, null=True)
    current_semester = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
