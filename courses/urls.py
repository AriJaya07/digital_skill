from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("add/", views.add_course, name="add_course"),
    path("<int:course_id>/", views.course_detail, name="course_detail"),
    path("edit/<int:course_id>/", views.edit_courses, name="edit_course"),
    path("delete/<int:course_id>/", views.delete_course, name="delete_course"),

    # materials
    path("<int:course_id>/materials/add/", views.material_add, name="material_add"),

    # enrollments
    path("<int:course_id>/enroll/", views.enroll_course, name="enroll_course"),
]