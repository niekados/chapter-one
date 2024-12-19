from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from djrichtextfield.models import RichTextField


class Author(models.Model):
    """
    Model to store author details.

    Fields:
        - name (CharField): The full name of the author.
        - birth_country (CountryField): The country where the author was born.
        - birth_date (DateField): The author's date of birth.
        - biography (RichTextField): A rich text biography of the author.
        - photo (ImageField): A photo of the author.
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    birth_country = CountryField(
        blank_label="Select country", null=False, blank=False
    )
    birth_date = models.DateField(null=False, blank=False)
    biography = RichTextField(null=False, blank=False)
    photo = models.ImageField(null=True, blank=True)

    def display_photo(self):
        """
        Display authors photo if available.
        If not available, return the placeholder image URL.
        """
        if self.photo:
            return self.photo.url
        return f'{settings.MEDIA_URL}placeholder_avatar.png'

    def __str__(self):
        return self.name
