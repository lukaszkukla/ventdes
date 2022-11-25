
from .forms import SubscribeNewsletterForm


def subscribe_form(request):
    form = SubscribeNewsletterForm()
    context = {'newsletter_form': form}
    return context
