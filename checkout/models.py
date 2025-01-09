from django.db import models
from uuid import uuid4
from django.db.models import Sum
from django_countries.fields import CountryField
from books.models import Book
from profiles.models import UserProfile


class Order(models.Model):
    """
    Model representing a customer's order.

    Fields:
        - order_number (CharField): A unique order number.
        - user_profile (ForeignKey): Links the order to the user's profile.
        - full_name (CharField): Full name of the customer.
        - email (EmailField): Customer's email address.
        - phone_number (CharField): Customer's contact number.
        - country (CountryField): Customer's country.
        - postcode (CharField): Customer's postal code. Optional.
        - town_or_city (CharField): Customer's town or city.
        - street_address1 (CharField): Customer's primary address.
        - street_address2 (CharField): Customer's secondary address. Optional.
        - county (CharField): Customer's county. Optional.
        - date (DateTimeField): Timestamp of when the order was created.
        - order_total (DecimalField): Total price of the order. Default is 0.
        - original_cart (TextField): JSON representation of the cart
        contents at checkout.
        - stripe_pid (CharField): Stripe Payment Intent ID for tracking
        the transaction.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)

    # Customer Information
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    # Address Details
    country = CountryField(
        blank_label='Country *', null=False, blank=False
    )
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_number(self):
        """ Generate unique order number using UUID """
        return uuid4().hex.upper()

    def update_total(self):
        """
        Update order total by summing up prices of all line items.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum('price'))['price__sum'] or 0
        )
        self.save()

    def save(self, *args, **kwargs):
        """ Add order number if it hasn't been added to order """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Model representing an individual book in a customer's order.

    Fields:
        - order (ForeignKey): Links the line item to its parent order.
        - book (ForeignKey): The purchased book.
        - price (DecimalField): Price of the book at the time of purchase.
    """
    order = models.ForeignKey(
        'Order',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    book = models.ForeignKey(
        Book, null=False, blank=False, on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )

    def save(self, *args, **kwargs):
        """Dynamically set the book's price."""
        self.price = self.book.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.book.title} (Order: {self.order.order_number})'
