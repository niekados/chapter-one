from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AuthorForm
from .models import Author


def authors_list(request):
    """
    View to display a list of all authors.
    """
    authors = Author.objects.all()
    return render(request, 'authors/authors_list.html', {'authors': authors})


@login_required
def add_author(request):
    """ A view for adding the author """
    if not request.user.is_superuser:
        messages.error(
            request, 'Access denied. This action is restricted to the \
            site owner. Please log in with an owner account.'
        )

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author has been added successfully!')
            return redirect(reverse('authors_list'))
        else:
            messages.error(
                request, 'There was an error adding the author. \
                Please check if the form is valid.'
            )
    else:
        form = AuthorForm()

    template = 'authors/add_author.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
