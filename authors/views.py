from django.shortcuts import render, redirect, reverse, get_object_or_404
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


@login_required
def edit_author(request, author_id):
    """ Edit authors profile """
    if not request.user.is_superuser:
        messages.error(
            request, 'Access denied. This action is restricted to the \
            site owner. Please log in with an owner account.'
        )

    author = get_object_or_404(Author, pk=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author has been successfully updated!')
            return redirect(reverse('authors_list'))
        else:
            messages.error(
                request, 'There was an error updating authors profile. \
                Please check if the form is valid.'
            )
    else:
        form = AuthorForm(instance=author)
        messages.info(
            request, f'Editting {author.name} profile'
        )

    template = 'authors/edit_author.html'
    context = {
        'form': form,
        'author': author,
    }

    return render(request, template, context)


@login_required
def delete_author(request, author_id):
    """ Delete the author """
    if not request.user.is_superuser:
        messages.error(
            request, 'Access denied. This action is restricted to the \
            site owner. Please log in with an owner account.'
        )
        return redirect(reverse('authors_list'))

    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    messages.success(
        request, f'Author "{author.name}" has been deleted successfully!'
    )

    return redirect(reverse('authors_list'))


@login_required
def confirm_delete_author(request, author_id):
    """ Confirm authors deletion """
    if not request.user.is_superuser:
        messages.error(
            request, 'Access denied. This action is restricted to the \
            site owner. Please log in with an owner account.'
        )
        return redirect(reverse('authors_list'))

    author = get_object_or_404(Author, pk=author_id)

    template = 'authors/confirm_author_delete.html'

    context = {
        'author': author,
    }

    return render(request, template, context)
