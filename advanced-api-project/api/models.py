from django.db import models

# Create your models here.

from django.core.exceptions import ValidationError
from datetime import date

class Author(models.Model):
    """
    Represents an author who can write multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book written by an author.
    Includes a title, publication year, and a link to the author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def clean(self):
        # Custom validation to ensure publication_year is not in the future
        if self.publication_year > date.today().year:
            raise ValidationError('Publication year cannot be in the future.')

    def __str__(self):
        return self.title
