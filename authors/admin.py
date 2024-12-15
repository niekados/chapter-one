from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin interface for Author model.
    """
    list_display = ['name', 'birth_country', 'birth_date']
    search_fields = ['name']
    ordering = ['name']
