from django.shortcuts import render, get_object_or_404
from .models import Tournament

# Create your views here.


def tournaments(request):
    tournaments = Tournament.objects.all()

    context = {
        'tournaments': tournaments,
    }

    return render(request, 'tournaments/tournaments.html', context)
