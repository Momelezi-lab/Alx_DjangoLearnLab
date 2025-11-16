from .models import Book
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown
    search_fields = ('title', 'author')                     # enable search
    list_filter = ('publication_year',)                     # enable filter

admin.site.register(Book, BookAdmin)
