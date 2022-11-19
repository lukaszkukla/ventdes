from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

from ventdes.settings import FREE_DELIVERY_THRESHOLD
from ventdes.settings import STANDARD_DELIVERY_PERCENTAGE


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    free_delivery_threshold = FREE_DELIVERY_THRESHOLD
    standard_delivery_percentage = STANDARD_DELIVERY_PERCENTAGE

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

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
