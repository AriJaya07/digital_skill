from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profiles/", views.profile_list, name="profile_list"),
    path("profiles/edit/<int:user_id>/", views.edit_profile, name="edit_profile"),
    path("me/", views.profile_detail, name="profile_detail"),
]