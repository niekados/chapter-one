from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import LibraryEntry


@login_required
def my_library(request):
    """View to display user's purchased books library"""
    library_entries = LibraryEntry.objects.filter(user=request.user)

    # Pagination
    paginator = Paginator(library_entries, 6)
    page = request.GET.get('page')
    library_entries = paginator.get_page(page)

    template = 'library/my_library.html'
    context = {
        'library_entries': library_entries,
    }

    return render(request, template, context)
