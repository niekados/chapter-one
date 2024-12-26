from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from books.models import Book


def view_cart(request):
    """ A view for shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, book_id):
    """ Add a book to the shopping cart """

    book = get_object_or_404(Book, pk=book_id)

    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if str(book_id) not in cart:
        cart[str(book_id)] = 1
        messages.success(request, f"'{book.title}' was added to your cart.")
    else:
        messages.warning(request, f"'{book.title}' is already in your cart.")

    request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, book_id):
    """ Remove a book from the shopping cart """

    try:
        book = get_object_or_404(Book, pk=book_id)

        cart = request.session.get('cart', {})

        if str(book_id) in cart:
            cart.pop(str(book_id))
            messages.success(
                request, f"Removed '{book.title}' from your cart."
            )
        else:
            messages.warning(request, f"'{book.title}' is not in your cart.")

        request.session['cart'] = cart

    except Exception as e:
        messages.error(request, f'Error removing book: {e}')

    return redirect('view_cart')
