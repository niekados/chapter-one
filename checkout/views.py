from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    View for handling checkout form submission and order creation.
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('books_list'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_publick_key': 'pk_test_51QaQS2C83Ur32NyyXdox0U7n6TBcTWHVkcEe7aQSvnVZ5hgmRUxlh6U6hraqR98K2DExoD49WmSC1yr9wSPG5t1F00Tpmv3md9',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
