from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

@login_required
def safe_book_search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # ORM handles parameterization
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Validate input
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
