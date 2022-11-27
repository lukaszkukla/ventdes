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
        self.fields["newsletter_email"].widget.attrs[
         "placeholder"] = "your@email.com"
        self.fields["newsletter_email"].widget.attrs[
         "class"] = "form-control"
        self.fields["newsletter_email"].error_messages[
         "required"] = "Please enter a valid email address"

        super(SubscribeNewsletterForm, self).__init__(*args, **kwargs)
        self.fields['newsletter_email'].label = False
        self.fields['newsletter_email'].widget.attrs.update({'placeholder': 'your@email.com'})
