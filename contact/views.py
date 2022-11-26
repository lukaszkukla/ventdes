from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail

from django.contrib.auth.models import User
from profiles.models import UserProfile
from .forms import ContactUsForm


def contact(request):
    """View to post user's message to Ventdes"""

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            name = form.data['name']
            email = form.data['email']
            subject = form.data['subject']
            message = form.data['message']
            recipient = [settings.EMAIL_HOST_USER]
            body = render_to_string(
                'contact/email/contact_message.txt',
                {'name': name, 'email': email, 'message': message}
            )
            try:
                send_mail(subject, body, email, recipient)
                messages.success(
                    request, f'Dear {email} thank you for your message. \
                        We will contact you shortly.'
                )
            except BadHeaderError:
                messages.error(
                    request, "Sorry - we are having issues with this request, \
                               please try again later"
                )

            return HttpResponseRedirect(reverse('contact'))
    else:
        try:
            user = User.objects.get(username=request.user)
            user_profile = get_object_or_404(UserProfile, user=user)
            form = ContactUsForm(
                initial={'email': user.email, 'name': user_profile.full_name}
            )
        except ObjectDoesNotExist:
            form = ContactUsForm()
    return render(request, 'contact/contact.html', {'form': form})
