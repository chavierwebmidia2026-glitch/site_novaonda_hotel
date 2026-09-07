from django.shortcuts import render
from .models import MenuHotel

from django.shortcuts import render


def index(request):

    return render(
        request,
        'index.html'
    )

def sobre(request):
    return render(request, 'sobre.html')