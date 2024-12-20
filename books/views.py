from django.shortcuts import render, get_object_or_404
from .models import Book


def all_books(request):
    """ A view to show a list of all books """
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/books_list.html', context)


def book_detail(request, slug):
    """ A detail view of an individual book """
    book = get_object_or_404(Book, slug=slug)
    context = {'book': book}
    return render(request, 'books/book_detail.html', context)
