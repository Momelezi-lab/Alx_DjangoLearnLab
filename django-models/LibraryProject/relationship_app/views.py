from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library

# -----------------------------------
# Function-based view: list all books
# -----------------------------------
def list_books(request):
    books = Book.objects.all()
    return render(
        request,
        "relationship_app/list_books.html",  # must match checker
        {"books": books}
    )

# -----------------------------------
# Class-based view: show details for a specific library
# -----------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # must match checker
    context_object_name = "library"

# -----------------------------------
# User Authentication
# -----------------------------------
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

# Registration view (function-based)
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Login view (class-based)
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

# Logout view (class-based)
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
