# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome to the blog.")
            return redirect("profile")
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("profile")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "blog/login.html")

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        email = request.POST.get("email")
        bio = request.POST.get("bio")
        profile_picture = request.FILES.get("profile_picture")

        user = request.user
        user.email = email
        user.save()

        profile.bio = bio
        if profile_picture:
            profile.profile_picture = profile_picture
        profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("profile")
    return render(request, "blog/profile.html", {"user": request.user, "profile": profile})