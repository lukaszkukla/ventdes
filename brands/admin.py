from django.contrib import admin
from .models import Brands


class BrandsAdmin(admin.ModelAdmin):
    """Admin class for Brands"""

    model = Brands


admin.site.register(Brands, BrandsAdmin)
