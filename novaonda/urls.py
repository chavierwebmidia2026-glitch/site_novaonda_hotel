from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos, name='servicos'),
    path('suites/',views.suites, name='suites'),
    path('galeria/', views.galeria, name='galeria'),
    path('cafe-da-manha/', views.cafe_da_manha, name='cafe_da_manha' ),
]
