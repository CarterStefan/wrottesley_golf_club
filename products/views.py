from django.shortcuts import render
from . models import Product

# Create your views here.


def all_products(request):
    """ A view for the products page, including different categories, searching and sorting """

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)
