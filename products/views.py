from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . models import Product, Category

# Create your views here.


def all_products(request):
    """ A view for the products page, including different categories, searching and sorting """

    products = Product.objects.all()
    all_categories = Category.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'filtered_category' in request.GET:
            categories = request.GET['filtered_category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter something to search the store!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'all_categories': all_categories,
        'current_categories': categories,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_information(request, product_id):
    """ A view to show an individual product detail """

    product = get_object_or_404(Product, pk=product_id)
    all_categories = Category.objects.all()

    context = {
        'product': product,
        'all_categories': all_categories,
    }

    return render(request, 'products/product_information.html', context)
