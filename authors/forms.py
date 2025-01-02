from djrichtextfield.widgets import RichTextWidget
from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):

    biography = forms.CharField(
        widget=RichTextWidget(),
        required=False
    )

    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Author
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'biography':
                field.widget.attrs['class'] = 'form-fields'
