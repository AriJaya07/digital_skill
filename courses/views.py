from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, CourseMaterial, Enrollment
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

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "course_detail.html", {"course": course})


# ---------- COURSE MATERIAL ----------
@login_required
def material_add(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        form = CourseMaterial(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.course = course
            material.save()
            return redirect("course_detail", pk=course.id)
    else:
        form = CourseMaterial()
    return render(request, "material_form.html", {"form": form, "course": course})

# ---------- ENROLLMENT ----------
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    Enrollment.objects.get_or_create(course=course, student=request.user)
    return redirect("course_detail", pk=course.id)