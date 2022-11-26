from django import forms
from .models import SubscribeNewsletter


class SubscribeNewsletterForm(forms.ModelForm):
    """Form for newsletter subscription"""

    class Meta:
        """Meta class SubscribeNewsletterForm"""
        model = SubscribeNewsletter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs[
         "placeholder"] = "your@email.com"
        self.fields["email"].widget.attrs[
         "class"] = "form-control"
        self.fields["email"].error_messages[
         "required"] = "Please enter a valid email address"

        super(SubscribeNewsletterForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = False
        self.fields['email'].widget.attrs.update({'placeholder': 'your@email.com'})
