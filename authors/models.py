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
        - photo (ImageField): An optional uploaded image for the author.
        - photo_url (URLField): An optional URL to the author's photo.
    """
    name = models.CharField(max_length=255, null=False, blank=False)
    birth_country = CountryField(
        blank_label="Select country", null=False, blank=False
    )
    birth_date = models.DateField(null=False, blank=False)
    biography = RichTextField(null=False, blank=False)
    photo = models.ImageField(null=True, blank=True)
    photo_url = models.URLField(max_length=1024, null=True, blank=True)

    def display_photo(self):
        """
        Return the uploaded image or image URL if available.
        If neither is available, return the placeholder image URL.
        """
        if self.photo:
            return self.photo.url
        elif self.photo_url:
            return self.photo_url
        return f'{settings.MEDIA_URL}placeholder_avatar.png'

    def __str__(self):
        return self.name
