from django.db import models


class Brands(models.Model):
    """
    Brands class
    """
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
