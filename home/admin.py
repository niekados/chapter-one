from django.contrib import admin
from .models import HomePageContent


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    """
    Admin interface for HomePageContent.
    """
    list_display = ['date_created', 'quote', 'quote_author']
    search_fields = ['quote', 'quote_author', 'about']
    list_filter = ['date_created']
    ordering = ['-date_created']
