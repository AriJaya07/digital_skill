from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "add_course.html", {"form": form})

def edit_courses(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm(instance=course)
    return render(request, "edit_course.html", {"form": form, "course": course})
    
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(request, "delete_course.html", {"course": course})