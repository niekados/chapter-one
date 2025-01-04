from django.contrib import admin
from .models import LibraryEntry


@admin.register(LibraryEntry)
class LibraryEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'purchase_date')
    list_filter = ('purchase_date', 'user')
    search_fields = ('user__username', 'book__title')
    ordering = ['-purchase_date']
