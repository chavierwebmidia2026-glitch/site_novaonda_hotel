from django.contrib import admin
from .models import MenuHotel

@admin.register(MenuHotel)
class MenuHotelAdmin(admin.ModelAdmin):

    list_display = (
        'ordem',
        'icone',
        'titulo',
        'ativo',
    )

    list_filter = (
        'ativo',
    )

    ordering = (
        'ordem',
    )