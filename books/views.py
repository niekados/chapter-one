from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Book, Genre
from .forms import BookForm


def all_books(request):
    """ A view to show a list of all books """

    books = Book.objects.all().order_by('-created_on')
    genres = Genre.objects.all()

    query = None
    selected_genre = None
    sort = None
    direction = None

    if request.GET:

        # Sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']

            if '_' in sortkey:
                sort, direction = sortkey.split('_')

            sort_field = sort
            if sort == 'title':
                books = books.annotate(lower_title=Lower('title'))
                sort_field = 'lower_title'
            elif sort == 'price':
                sort_field = 'price'
            elif sort == 'latest':
                sort_field = 'created_on'
            elif sort == 'author':
                books = books.annotate(lower_author=Lower('author__name'))
                sort_field = 'lower_author'

            if direction == 'desc':
                sort_field = f'-{sort_field}'

            books = books.order_by(sort_field)

        # Filtering by genre
        if 'genre' in request.GET:
            selected_genre = request.GET['genre']
            if selected_genre:
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

    current_sorting = request.GET.get('sort', 'latest_desc')

    # Pagination
    paginator = Paginator(books, 6)
    page = request.GET.get('page')
    books = paginator.get_page(page)

    context = {
        'books': books,
        'genres': genres,
        'search_keyword': query,
        'current_genre': selected_genre,
        'current_sorting': current_sorting,
    }

    return render(request, 'books/books_list.html', context)


def book_detail(request, slug):
    """ A detail view of an individual book """

    book = get_object_or_404(Book, slug=slug)

    cart = request.session.get('cart', {})

    book_in_cart = str(book.id) in cart

    context = {
        'book': book,
        'book_in_cart': book_in_cart,
    }

    return render(request, 'books/book_detail.html', context)


def add_book(request):
    """ A view for adding the book """
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book has been added successfully!')
            return redirect(reverse('add_book'))
        else:
            messages.error(
                request, 'There was an error adding the book. \
                Please check if the form is valid.'
            )
    else:
        form = BookForm()

    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
