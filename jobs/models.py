from django.db import models
from accounts.models import User
from courses.models import Skill

class Job(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'employer'})
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.ManyToManyField(Skill)
    location = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='job_images/', blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(
        ("pending", "Pending"),
        ("reviewed", "Reviewed"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ), default="pending")
