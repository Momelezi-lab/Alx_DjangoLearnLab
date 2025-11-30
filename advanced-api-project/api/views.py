from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books - accessible to anyone
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Returns a list of all books.
    Read-only view, open to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<int:pk>/
    Returns details of a single book.
    Read-only, open to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<int:pk>/update/
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<int:pk>/delete/
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
