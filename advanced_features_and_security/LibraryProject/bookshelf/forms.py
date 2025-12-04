from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

    # Optional: additional input validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title
