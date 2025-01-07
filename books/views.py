from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from library.models import LibraryEntry
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
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    books = paginator.get_page(page)

    template = 'books/books_list.html'

    context = {
        'books': books,
        'genres': genres,
        'search_keyword': query,
        'current_genre': selected_genre,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def book_detail(request, slug):
    """ A detail view of an individual book """

    book = get_object_or_404(Book, slug=slug)

    cart = request.session.get('cart', {})

    book_in_cart = str(book.id) in cart

    # Check if user owns a book
    user_owns_book = False
    if request.user.is_authenticated:
        user_owns_book = LibraryEntry.objects.filter(
            user=request.user,
            book=book
        ).exists()

    template = 'books/book_detail.html'

    context = {
        'book': book,
        'book_in_cart': book_in_cart,
        'user_owns_book': user_owns_book,
    }

    return render(request, template, context)


@login_required
def owner_manage_books(request):
    """ View to display a list of all books for site owner """
    if not request.user.is_superuser:
        messages.error(
            request, 'Access denied. This action is restricted to the \
            site owner. Please log in with an owner account.'
        )
        return redirect(reverse('books_list'))
    books = books = Book.objects.all().order_by('title')
    template = 'books/manage_books.html'
    context = {'books': books}
    return render(request, template, context)


@login_required
def add_book(request):
    """ A view for adding the book """
    if not request.user.is_superuser:
        messages.error(
            request, 'Access denied. This action is restricted to the \
            site owner. Please log in with an owner account.'
        )

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book has been added successfully!')
            return redirect(reverse('book_detail', kwargs={'slug': book.slug}))
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


@login_required
def edit_book(request, slug):
    """ Edit existing book """
    if not request.user.is_superuser:
        messages.error(
            request, 'Access denied. This action is restricted to the \
            site owner. Please log in with an owner account.'
        )

    book = get_object_or_404(Book, slug=slug)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book has been successfully updated!')
            return redirect(reverse('book_detail', kwargs={'slug': book.slug}))
        else:
            messages.error(
                request, 'There was an error updating the book. \
                Please check if the form is valid.'
            )
    else:
        form = BookForm(instance=book)
        messages.info(
            request, f'Editting book "{book.title}" by {book.author}'
        )

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)


@login_required
def delete_book(request, book_id):
    """ Delete the book """
    if not request.user.is_superuser:
        messages.error(
            request, 'Access denied. This action is restricted to the \
            site owner. Please log in with an owner account.'
        )
        return redirect(reverse('books_list'))

    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(
        request, f'Book "{book.title}" has been deleted successfully!'
    )

    return redirect(reverse('manage_books'))


@login_required
def confirm_delete_book(request, book_id):
    """ Confirm book deletion """
    if not request.user.is_superuser:
        messages.error(
            request, 'Access denied. This action is restricted to the \
            site owner. Please log in with an owner account.'
        )
        return redirect('books_list')

    book = get_object_or_404(Book, pk=book_id)

    template = 'books/confirm_book_delete.html'

    context = {
        'book': book,
    }

    return render(request, template, context)
