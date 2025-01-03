from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from books.models import Book
from profiles.models import UserProfile
from library.models import LibraryEntry
from django.contrib.auth.models import User
import json
import time
import stripe


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send Order Confirmation email """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic, unknown or unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        order_total = round(stripe_charge.amount / 100, 2)

        # Clean billing details data
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        # Update profile info when save_info is checked
        profile = None
        username = intent.metadata.username

        # Make sure user is authenticated
        if username == 'AnonymousUser':
            return HttpResponse(
                content='Webhook received: AnonymousUser \
                    cannot purchase books.',
                status=400
            )

        # Fetch the authenticated user
        user = User.objects.get(username=username)

        profile = UserProfile.objects.get(user__username=username)
        if save_info:
            profile.default_phone_number = billing_details.phone
            profile.default_country = billing_details.address.country
            profile.default_postcode = billing_details.address.postal_code
            profile.default_town_or_city = billing_details.address.city
            profile.default_street_address1 = billing_details.address.line1
            profile.default_street_address2 = billing_details.address.line2
            profile.default_county = billing_details.address.state
            profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    postcode__iexact=billing_details.address.postal_code,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    county__iexact=billing_details.address.state,
                    order_total=order_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:

            # Add books to users library
            for line_item in order.lineitems.all():
                LibraryEntry.objects.get_or_create(
                    user=user,
                    book=line_item.book,
                )

            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                    Verified order already in database',
                status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for book_id in json.loads(cart).keys():
                    book = Book.objects.get(id=book_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        book=book,
                    )
                    order_line_item.save()

                    # Add books to user's library
                    LibraryEntry.objects.get_or_create(
                        user=user,
                        book=book,
                    )

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500
                    )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: \
                Order created in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
