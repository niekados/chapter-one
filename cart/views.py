from django.shortcuts import render, redirect


def view_cart(request):
    """ A view for shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, book_id):
    """ Add a book to the shopping cart """

    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if book_id not in cart:
        cart[book_id] = 1

    request.session['cart'] = cart

    return redirect(redirect_url)
