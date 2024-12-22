

def cart_contents(request):

    cart_items = []
    total = 0
    books_count = 0

    context = {
        'cart_items': cart_items, 
        'total': total,
        'books_count': books_count,
    }

    return context
