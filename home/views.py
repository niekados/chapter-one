from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import HomePageContent


def index(request):
    """A view to return the index page with contact form"""

    content = HomePageContent.objects.first() or {
        "quote": "Poetry is what happens when nothing else can.",
        "quote_author": "Charles Bukowski",
        "about": (
            "Chapter One is a platform for discovering digital books by "
            "emerging authors. We help new writers publish their "
            "stories at an affordable price, making literature "
            "accessible to everyone."
        ),
    }

    # Handle contact form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_subject = f"New Contact Form Submission: {subject}"
            email_body = (
                f"Name: {name}\n"
                f"Email: {email}\n\n"
                f"Message:\n{message}"
            )

            try:
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )

                user_subject = "Thank you for contacting Chapter One!"
                user_body = (
                    f"Hello {name},\n\n"
                    "Thank you for reaching out to us! We've received your "
                    "message and will get back to you as soon as possible.\n\n"
                    "Best regards,\nThe Chapter One Team"
                )
                send_mail(
                    user_subject,
                    user_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                messages.success(
                    request, 'Your message has been sent successfully!'
                )
                return redirect('home')

            except Exception:
                messages.error(
                    request, 'Failed to send email! Please try again later.'
                )

        else:
            messages.error(
                request, 'There was a problem submitting your form. \
                    Please try again.'
            )
    else:
        form = ContactForm()

    context = {
        'content': content,
        'form': form,
    }

    return render(request, 'home/index.html', context)
