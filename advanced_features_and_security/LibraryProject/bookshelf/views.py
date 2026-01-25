from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # logic to create book
    return render(request, 'bookshelf/book_form.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    # logic to edit book
    return render(request, 'bookshelf/book_form.html')


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    # logic to delete book
    return render(request, 'bookshelf/book_confirm_delete.html')
