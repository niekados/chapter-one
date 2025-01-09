from django.db import models
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Represents a user profile containing default delivery information.

    Fields:
        - user (OneToOneField): Links the profile to a Django User model.
        - default_phone_number (CharField): User's phone number. Optional.
        - default_street_address1 (CharField): User's primary street address.
        Optional.
        - default_street_address2 (CharField): User's secondary street address.
        Optional.
        - default_town_or_city (CharField): User's town or city. Optional.
        - default_county (CharField): User's county. Optional.
        - default_postcode (CharField): User's postal code. Optional.
        - default_country (CountryField): User's country. Optional.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    default_county = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True
    )
    default_country = CountryField(
        blank_label='Country', null=True, blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Save profile for existing users
    instance.userprofile.save()
