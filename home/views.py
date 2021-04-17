from django.shortcuts import render
from profiles.models import UserProfile
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    """ A view to display the index page """

    membership_level = None

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        membership_level = profile.membership_type

    context = {
            'membership_level': membership_level,
        }

    return render(request, 'home/index.html', context)
