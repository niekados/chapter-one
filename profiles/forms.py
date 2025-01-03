from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for collecting user details during checkout.
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, autofocus, and styling for each form field.
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'default_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
