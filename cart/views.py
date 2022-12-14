from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """A view that renders the cart content"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the product to the shopping cart """
    try:
        quantity = int(request.POST.get('quantity'))
    except Exception as e:
        messages.warning(
                    request, f'Qantity must be a numeric value'
                )
        return redirect(reverse('product_details', args=[item_id]))

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if cart[item_id] >= 9999:
            cart[item_id] = 9999
            messages.warning(
                request, f'Updated {product.name} to maximum quantity \
                    allowed {cart[item_id]}'
            )
        else:
            cart[item_id] += quantity
            total = cart[item_id]
            if total >= 9999:
                cart[item_id] = 9999
                messages.warning(
                    request, f'Updated {product.name} to maximum quantity \
                        allowed {cart[item_id]}'
                )
            else:
                cart[item_id] += quantity
                messages.success(
                    request, f'Updated {product.name} \
                        quantity to {cart[item_id]}'
                )
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to the cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the product in the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        if quantity > 9999:
            cart[item_id] = 9999
            messages.warning(
                request, f'Updated {product.name} quantity to \
                    maximum allowed {cart[item_id]}'
            )
        else:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}'
            )
    elif quantity > 9999:
        quantity = 9999
        cart[item_id] = quantity

    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from the cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the product from the shopping cart """
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from the cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
