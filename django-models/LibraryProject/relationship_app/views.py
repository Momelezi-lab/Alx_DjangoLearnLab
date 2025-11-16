from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# -------------------------------
# Function-Based View (FBV)
# -------------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# -------------------------------
# Class-Based View (CBV)
# -------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

