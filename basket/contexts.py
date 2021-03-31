from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from profiles.models import UserProfile


def basket_contents(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    membership_level = profile.membership_type

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            for size, quantity in item_data['items_by_size'].items():
                product = get_object_or_404(Product, pk=item_id)
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if membership_level == 'Pro':
        discount = total * Decimal(settings.PRO_STORE_DISCOUNT / 100)
        delivery = total * Decimal(settings.PRO_DELIVERY_CHARGE / 100)
    elif membership_level == 'Beginner':
        discount = total * Decimal(settings.BEGINNER_STORE_DISCOUNT / 100)
        delivery = total * Decimal(settings.BEGINNER_DELIVERY_CHARGE / 100)
    else:
        discount = total * Decimal(settings.BEGINNER_STORE_DISCOUNT / 100)
        delivery = total * Decimal(settings.BEGINNER_DELIVERY_CHARGE / 100)

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
