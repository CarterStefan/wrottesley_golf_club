from django.shortcuts import render
from profiles.models import UserProfile
from .models import Tournament

# Create your views here.


def tournaments(request):
    tournaments = Tournament.objects.all()

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            membership = profile.membership_type
        except UserProfile.DoesNotExist:
            membership = 'Beginner'
    else:
        membership = 'Beginner'

    context = {
        'tournaments': tournaments,
        'membership': membership,
    }

    return render(request, 'tournaments/tournaments.html', context)
