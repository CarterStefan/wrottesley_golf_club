from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view for the products page, including different categories, searching and sorting """

    products = Product.objects.all()
    categories = Category.objects.all()
    search_term = None
    current_category = None
    current_category_upper = None
    direction = None
    sort = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Filter the products to show only those in the selected category
        if 'category' in request.GET:
            current_category = request.GET['category']
            products = products.filter(category__name=current_category)
            current_category_upper = current_category.capitalize()

        # Filter the products to show only those that match the search terms
        if 'search' in request.GET:
            search_term = request.GET['search']
            if not search_term:
                messages.error(request, "Please enter something to search the store!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=search_term) | Q(description__icontains=search_term) | Q(category__name__icontains=search_term)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'categories': categories,
        'search_term': search_term,
        'current_category': current_category,
        'current_sorting': current_sorting,
        'current_category_upper': current_category_upper,
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
