from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile
from .models import Tournament

# Create your views here.


def tournaments(request):
    tournaments = Tournament.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)
    membership = profile.membership_type

    context = {
        'tournaments': tournaments,
        'membership': membership,
    }

    return render(request, 'tournaments/tournaments.html', context)
