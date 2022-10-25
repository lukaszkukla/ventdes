from decimal import Decimal
from django.conf import settings

from ventdes.settings import FREE_DELIVERY_THRESHOLD


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    standard_delivery_percentage = settings.STANDARD_DELIVERY_PERCENTAGE

    if total < free_delivery_threshold:
        delivery = total * Decimal(standard_delivery_percentage / 100)
        free_delivery_delta = free_delivery_threshold - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
    }

    return context
