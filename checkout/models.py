from django.db import models
from uuid import uuid4
from django.db.models import Sum
from books.models import Book


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)

    # Customer Information
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    # Address Details
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
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

    def __str__(self):
        return f'{self.book.title} (Order: {self.order.order_number})'