from django import forms

# https://docs.djangoproject.com/en/4.0/topics/forms/


class ContactUsForm(forms.Form):
    """Form to collect contact details and the message"""

    name = forms.CharField(
        label='Name',
        required=True,
        min_length=3, max_length=50,
        error_messages={'required': 'Please enter your name'}
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=254,
        error_messages={'required': 'Please enter a valid email address'}
    )

    subject = forms.CharField(
        label='Subject',
        required=False,
        max_length=254,
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '60', 'rows': '15'}),
        label='Message',
        required=True,
        min_length=3, max_length=2000,
        error_messages={'required': 'Please enter your message'}
    )
