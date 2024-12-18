from django.contrib import admin
from .models import Book, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Admin interface for the Genre model.
    """
    list_display = ['friendly_name', 'name']
    search_fields = ['friendly_name', 'name']
    ordering = ['friendly_name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin interface for the Book model.
    """
    list_display = ['title', 'author', 'genre', 'price', 'created_on']
    search_fields = [
        'title', 'author__name', 'genre__friendly_name', 'description'
    ]
    list_filter = ['genre', 'author', 'created_on']
    ordering = ['title']
