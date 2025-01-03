from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class LibraryEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='library'
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Library Entries'
        unique_together = ['user', 'book']
        ordering = ['-purchase_date']

    def __str__(self):
        user_display = self.user.username if self.user else "Deleted User"
        return f"{user_display}'s copy of {self.book.title}"
