from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . models import Product, Category

# Create your views here.


def all_products(request):
    """ A view for the products page, including different categories, searching and sorting """

    products = Product.objects.all()
    all_categories = Category.objects.all()
    search_term = None
    selected_category = None

    if request.GET:
        # Filter the products to show only those in the selected category
        if 'filtered_category' in request.GET:
            selected_category = request.GET['filtered_category']
            products = products.filter(category__name=selected_category)
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                if selected_category is None:
                    products = Product.objects.order_by(sortkey)

                products = products.order_by(sortkey)

        # Filter the products to show only those that match the search terms
        if 'search' in request.GET:
            search_term = request.GET['search']
            if not search_term:
                messages.error(request, "Please enter something to search the store!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=search_term) | Q(description__icontains=search_term) | Q(category__name__icontains=search_term)
            products = products.filter(queries)

    context = {
        'products': products,
        'all_categories': all_categories,
        'selected_category': selected_category,
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
