from django.contrib import admin
from .models import MenuHotel, Suite, Foto, CafeDaManha, Servico, Contato

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


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):

    list_display = (
        'ordem',
        'titulo',
        'ativo',
    )

    list_filter = (
        'ativo',
    )

    ordering = (
        'ordem',
    )


@admin.register(CafeDaManha)
class CafeDaManhaAdmin(admin.ModelAdmin):

    list_display = (
        'ordem',
        'nome',
        'ativo',
    )

    list_filter = (
        'ativo',
    )

    ordering = (
        'ordem',
    )



@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)



@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'email',
        'telefone',
        'assunto',
        'data_envio',
    )

    list_filter = (
        'data_envio',
    )

    search_fields = (
        'nome',
        'email',
        'assunto',
        'mensagem',
    )

    ordering = (
        '-data_envio',
    )