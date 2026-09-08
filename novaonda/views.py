from django.shortcuts import render

from .models import MenuHotel, Suite, Foto, CafeDaManha, Servico, Contato


def index(request):

    return render(
        request,
        'index.html'
    )


def sobre(request):

    return render(
        request,
        'sobre.html'
    )


def contato(request):

    if request.method == 'POST':

        Contato.objects.create(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            assunto=request.POST.get('assunto'),
            mensagem=request.POST.get('mensagem'),
        )

        return render(
            request,
            'contato.html',
            {
                'sucesso': True
            }
        )

    return render(
        request,
        'contato.html'
    )


def servicos(request):

    servicos = Servico.objects.filter(ativo=True)

    return render(
        request,
        'servicos.html',
        {
            'servicos': servicos
        }
    )

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


def galeria(request):

    fotos = Foto.objects.filter(
        ativo=True
    ).order_by('ordem')

    context = {
        'fotos': fotos,
    }

    return render(
        request,
        'galeria.html',
        context
    )


def cafe_da_manha(request):

    cafes = CafeDaManha.objects.filter(
        ativo=True
    ).order_by('ordem')

    context = {
        'cafes': cafes,
    }

    return render(
        request,
        'cafe_da_manha.html',
        context
    )