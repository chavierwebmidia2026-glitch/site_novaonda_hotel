from django.shortcuts import render
from .models import MenuHotel
from .models import Suite

from django.shortcuts import render


def index(request):

    return render(
        request,
        'index.html'
    )

def sobre(request):
    return render(request, 'sobre.html')


def suites(request):

    suites = Suite.objects.filter(
        ativo=True
    ).order_by('ordem')

    context = {
        'suites': suites,
    }

    return render(
        request,
        'suites.html',
        context
    )