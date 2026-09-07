from .models import MenuHotel


def menu_hotel(request):

    return {
        'menu_hotel': MenuHotel.objects.filter(
            ativo=True
        ).order_by('ordem')
    }