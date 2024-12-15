from django.shortcuts import render
from .models import Author


def authors_list(request):
    """
    View to display a list of all authors.
    """
    authors = Author.objects.all()
    return render(request, 'authors/authors_list.html', {'authors': authors})
