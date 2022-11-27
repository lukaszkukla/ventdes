from django.shortcuts import render
from .models import Brands


def all_brands(request):
    """ A view to show all brands """

    brands = Brands.objects.all()
    query = None

    context = {
        'brands': brands,
    }

    return render(request, 'brands/brands.html', context)
