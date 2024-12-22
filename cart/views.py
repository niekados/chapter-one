from django.shortcuts import render


def view_cart(request):
    """ A view for shopping cart """

    return render(request, 'cart/cart.html')
