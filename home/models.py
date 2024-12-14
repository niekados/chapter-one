from django.db import models
from djrichtextfield.models import RichTextField


class HomePageContent(models.Model):
    """
    Model for the content displayed on the homepage.

    Fields:
        - quote (TextField): The literary quote shown on the homepage.
        - quote_author (CharField): The author of the quote.
        - about (RichTextField): The 'About Us' section content.
        - date_created (DateTimeField): The timestamp for when this
          content was created.
    """
    quote = models.TextField(null=False, blank=False)
    quote_author = models.CharField(
        max_length=255, default="Unknown", null=False, blank=False
    )
    about = RichTextField(null=False, blank=False)
    date_created = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return f"Homepage Content - {self.quote_author} - {self.date_created}"
