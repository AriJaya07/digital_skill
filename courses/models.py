from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    skill = models.ForeignKey("courses.Skill", on_delete=models.CASCADE, related_name='courses')
    mentor = models.ForeignKey("accounts.User", on_delete=models.CASCADE, limit_choices_to={'role': 'mentor'})
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
