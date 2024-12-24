from django.shortcuts import render, redirect


def view_cart(request):
    """ A view for shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, book_id):
    """ Add a book to the shopping cart """

    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if str(book_id) not in cart:
        cart[str(book_id)] = 1

    request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, book_id):
    """ Remove a book from the shopping cart """

    cart = request.session.get('cart', {})

    if str(book_id) in cart:
        cart.pop(str(book_id))

    request.session['cart'] = cart

    return redirect('view_cart')
