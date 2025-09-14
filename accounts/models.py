from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("student", "Student"),
        ("mentor", "Mentor"),
        ("employer", "Employer"),
        ("admin", "Admin")
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField("courses.Skill", blank=True)

