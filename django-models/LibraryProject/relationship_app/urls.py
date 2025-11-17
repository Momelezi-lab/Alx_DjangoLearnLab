from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # Existing book/library URLs
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Custom permission URLs
    path('book/add/', add_book, name='add_book'),
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),
]

