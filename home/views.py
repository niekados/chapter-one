from django.shortcuts import render
from .models import HomePageContent


def index(request):
    """A view to return the index page """
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
    return render(request, 'home/index.html', {'content': content})
