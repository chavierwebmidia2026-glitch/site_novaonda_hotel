from django.contrib import admin
from .models import MenuHotel, Suite

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
    

@admin.register(Suite)
class SuiteAdmin(admin.ModelAdmin):

    list_display = (
        'ordem',
        'nome',
        'capacidade',
        'preco',
        'ativo',
    )

    list_filter = (
        'ativo',
    )

    ordering = (
        'ordem',
    )