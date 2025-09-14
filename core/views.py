# core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course
from jobs.models import Job

def home(request):
    courses = Course.objects.all()
    jobs = Job.objects.all()
    return render(request, "home.html", {
        "courses": courses,
        "jobs": jobs
    })
