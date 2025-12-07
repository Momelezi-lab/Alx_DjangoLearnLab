# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4, "placeholder": "Write your comment here..."}),
        }

    def clean_content(self):
        content = self.cleaned_data["content"]
        if len(content) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        if len(content) > 1000:
            raise forms.ValidationError("Comment cannot exceed 1000 characters.")
        return content

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter post title"}),
            "content": forms.Textarea(attrs={"rows": 6, "placeholder": "Write your post content..."}),
            "tags": forms.TextInput(attrs={"placeholder": "Enter tags, separated by commas"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title