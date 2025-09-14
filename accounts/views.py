from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm, ProfileForm
from .models import User

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render("home")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render("home")

def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def profile_list(request):
    users = User.objects.all()
    return render(request, "profile_list.html", {"users": users})

@login_required
def edit_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.user != user and request.user.role != "admin":
        return redirect("home")
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile_list")
        
    else:
        form = ProfileForm(instance=user)

    return render(request, "edit_profile.html", {"form": form, "user_obj": user})

@login_required
def profile_detail(request):
    user = request.user

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile_detail")
    else:
        form = ProfileForm(instance=user)

    return render(request, "profile_detail.html", {"form": form, "user_obj": user})