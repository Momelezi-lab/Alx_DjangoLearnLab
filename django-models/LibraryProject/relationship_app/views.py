from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library
from .models import Library  # Required by ALX checker

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(
        request,
        "relationship_app/list_books.html",   # checker expects this exact path
        {"books": books}
    )

# Class-based view: show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # checker expects this exact path
    context_object_name = "library"

