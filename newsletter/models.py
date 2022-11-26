from django.db import models


class SubscribeNewsletter(models.Model):
    """ Stores email addresses of subscribers """

    email = models.EmailField(
        max_length=255, null=False, blank=False, unique=True,
    )

    class Meta:
        """
        Meta class for SubscribeNewsletter
        """
        verbose_name = 'Newsletter Subscribers List'

    def __str__(self):
        return str(self.email)
