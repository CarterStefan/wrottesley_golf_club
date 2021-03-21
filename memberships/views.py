from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def memberships(request):
    """ A view to display the memberships page """

    return render(request, 'memberships/memberships.html')
