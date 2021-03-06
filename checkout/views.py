from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There is currently no items in your basket")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I8qYXHhFcVwa3bqdsevZsfKQonHZUMiRGNSy6QUOcFBW4cjfiYvGgaSaAJqHUkmnRfYPPdCPH7E6ZuaOxQvwAqA00hMrkyQcI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
