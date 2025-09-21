from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("<int:job_id>/", views.job_detail, name="job_detail"),
    path("add/", views.add_job, name="add_job"),
    path("edit/<int:job_id>/", views.edit_job, name="edit_job"),
    path("delete/<int:job_id>/", views.delete_job, name="delete_job"),
    path("<int:job_id>/apply/", views.apply_job, name="apply_job"),
]