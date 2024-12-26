from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin to manage line items inside Order admin.
    """
    model = OrderLineItem
    readonly_fields = ('price',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface for Order model.
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'order_total')
    fields = (
        'order_number', 'date', 'full_name', 'email', 'phone_number',
        'country', 'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'county', 'order_total'
    )
    list_display = (
        'order_number', 'date', 'full_name', 'order_total'
    )
    ordering = ('-date',)
