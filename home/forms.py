from django import forms


class ContactForm(forms.Form):
    """ Contact form for users to send messages. """

    SUBJECT_CHOICES = [
        ('', 'Select a Subject'),
        ('general', 'General Inquiry'),
        ('support', 'Support Request'),
        ('publish', 'Publish Book'),
        ('feedback', 'Feedback'),
    ]

    name = forms.CharField(
        max_length=255,
        required=True,
    )
    email = forms.EmailField(
        required=True,
    )
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        required=True,
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 4})
    )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, autofocus, and custom styles for form fields.
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Your Name',
            'email': 'Your Email Address',
            'subject': 'Select a Subject',
            'message': 'Write your message here...',
        }

        for field in self.fields:
            if field != 'subject':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].label = False
