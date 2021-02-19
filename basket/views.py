from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ A view to display the items added to the basket """

    return render(request, 'basket/basket.html')
