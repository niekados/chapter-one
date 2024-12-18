from django.db import models
from django.utils.text import slugify
from authors.models import Author


class Genre(models.Model):
    """
    Model to represent book genres.

    Fields:
        - name (CharField): The programmatic name of the genre.
        - friendly_name (CharField): The user friendly name of the genre.
    """
    name = models.CharField(
        max_length=100, unique=True, null=False, blank=False
    )
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Format the 'name' field and generate the 'friendly_name' if missing.
        """
        # Replace spaces with underscores and convert to lowercase
        self.name = self.name.lower().replace(" ", "_")

        # Generate friendly_name if it's blank
        if not self.friendly_name:
            self.friendly_name = self.name.replace("_", " ").title()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.friendly_name


class Book(models.Model):
    """
    Model to represent books.

    Fields:
        - title (CharField): The title of the book.
        - slug (SlugField): URL-friendly identifier for the book.
        - author (ForeignKey): Links the book to its author.
        - genre (ForeignKey): Links the book to a genre.
        - description (TextField): A brief description of the book.
        - price (DecimalField): The price of the book.
        - file (FileField): The uploaded book file (stored in AWS S3).
        - created_on (DateTimeField): The date the book was added.
    """
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, null=False, blank=False
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, null=False, blank=False
    )
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False
    )
    file = models.FileField(upload_to='books/', null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Generate slug from title if not entered.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
