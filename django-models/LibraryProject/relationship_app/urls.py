from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # Existing views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Custom permission views
    path('add_book/', add_book, name='add_book'),           # MUST contain "add_book/"
    path('edit_book/<int:pk>/', edit_book, name='edit_book'), # MUST contain "edit_book/"
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]

