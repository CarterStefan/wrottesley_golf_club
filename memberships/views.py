from django.shortcuts import render

# Create your views here.


def memberships(request):
    """ A view to display the memberships page """

    return render(request, 'memberships/memberships.html')
