from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    membership_level = 'pro'

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if membership_level == 'pro':
        discount = total * Decimal(settings.PRO_STORE_DISCOUNT / 100)
        delivery = total * Decimal(settings.PRO_DELIVERY_CHARGE / 100)
    elif membership_level == 'amateur':
        discount = total * Decimal(settings.AMATEUR_STORE_DISCOUNT / 100)
        delivery = total * Decimal(settings.AMATEUR_DELIVERY_CHARGE / 100)
    else:
        discount = total * Decimal(settings.AMATEUR_STORE_DISCOUNT / 100)
        delivery = total * Decimal(settings.PRO_DELIVERY_CHARGE / 100)

    grand_total = total - discount + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'delivery': delivery,
        'grand_total': grand_total,
        'membership_level': membership_level,
    }

    return context
