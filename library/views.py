from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import LibraryEntry


@login_required
def my_library(request):
    """View to display user's purchased books library"""
    library_entries = LibraryEntry.objects.filter(user=request.user)

    # Pagination
    paginator = Paginator(library_entries, 8)
    page = request.GET.get('page')
    library_entries = paginator.get_page(page)

    template = 'library/my_library.html'
    context = {
        'library_entries': library_entries,
    }

    return render(request, template, context)


def download_book(request, book_id):
    """ View for downloading books owned by the user """
    try:
        library_entry = get_object_or_404(
            LibraryEntry,
            user=request.user,
            book_id=book_id
        )

        book = library_entry.book

        try:
            response = FileResponse(
                book.file.open('rb'),
                content_type='application/pdf'
            )
            response['Content-Disposition'] = f'attachment; \
                filename="{book.title}.pdf"'
            return response
        except FileNotFoundError:
            raise Http404("Book file not found")
    except Exception:
        messages.error(
            request, "You must purchase this book before downloading."
        )
        return HttpResponse('Book not found or not purchased.', status=404)
