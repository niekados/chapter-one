from django.shortcuts import get_object_or_404
from books.models import Book


def cart_contents(request):

    cart_items = []
    total = 0

    cart = request.session.get('cart', {})

    for book_id in cart.keys():
        book = get_object_or_404(Book, pk=book_id)
        total += book.price
        cart_items.append({
            'book_id': book_id,
            'book': book,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return context
