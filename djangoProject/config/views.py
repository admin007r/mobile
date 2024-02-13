from django.contrib.auth.models import User
from django.shortcuts import render

from django.views.generic import ListView
from .models import Bee, Ucell, Mobi


# Create your views here.
def index(request):
    bee = Bee.objects.all()
    ucell = Ucell.objects.all()
    mobi = Mobi.objects.all()
    context = {
        'bee': bee,
        'ucell': ucell,
        'mobi': mobi
    }
    return render(request, 'home.html', context)
