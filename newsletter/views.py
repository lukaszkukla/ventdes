from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from profiles.models import UserProfile

from .forms import SubscribeNewsletterForm


def subscribe_newsletter(request):
    """Subscribe to newsletter list"""

    if request.method == 'POST':

        form = SubscribeNewsletterForm(request.POST)

        if form.is_valid():

            form.save()
            confirmation_msg = 'Thank you for signing up!'
            sender = settings.EMAIL_HOST_USER
            recipient = [form.cleaned_data['email']]
            email_subject = confirmation_msg
            email_body = render_to_string(
                'newsletter/confirmation_emails/confirmation_email_body.txt'
            )

            try:
                existing_user = User.objects.get(email=form.cleaned_data[
                                                'email'])
            except ObjectDoesNotExist:
                existing_user = None

            if existing_user:
                profile = UserProfile.objects.get(user=existing_user)
                if profile and not profile.subscribe_newsletter:
                    profile.subscribe_newsletter = True
                    profile.save()
            messages.success(request, confirmation_msg)
            try:
                send_mail(email_subject, email_body, sender, recipient)
            except BadHeaderError:
                messages.error(
                    request, "Sorry - we are having issues with this request, \
                               please try again later"
                )
        else:
            messages.warning(request,
                             'You have already subscribed to our newsletter')
    return redirect(reverse('home'))
