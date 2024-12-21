from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book, Genre


def all_books(request):
    """ A view to show a list of all books """

    books = Book.objects.all()
    genres = Genre.objects.all()
    query = None
    selected_genre = None

    # Categories
    if request.GET:
        if 'genre' in request.GET:
            selected_genre = request.GET['genre']
            books = books.filter(genre__name=selected_genre)

        # Search functionality
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search word entered!")
                return redirect(reverse('books_list'))

            queries = (
                Q(title__icontains=query) |
                Q(author__name__icontains=query) |
                Q(description__icontains=query)
            )
            books = books.filter(queries)

    context = {
        'books': books,
        'genres': genres,
        'search_keyword': query,
        'current_genre': selected_genre,
    }

    return render(request, 'books/books_list.html', context)


def book_detail(request, slug):
    """ A detail view of an individual book """

    book = get_object_or_404(Book, slug=slug)

    context = {'book': book}

    return render(request, 'books/book_detail.html', context)
