from django.contrib import admin
from .models import SubscribeNewsletter


class SubscribeNewsletterAdmin(admin.ModelAdmin):
    """Admin class for Newsletter"""

    model = SubscribeNewsletter
    email_list = ('email', )


admin.site.register(SubscribeNewsletter, SubscribeNewsletterAdmin)
