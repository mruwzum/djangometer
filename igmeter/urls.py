from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    # path('cargar/', views.cargar, name='cargar'),
    # path('noticias/', views.noticias, name='noticas'),
    # path('top3/', views.relevancia, name='top3'),
    # path('busqueda/', views.busqueda, name='busqueda'),
    # path('recomienda/', views.recomendadas, name='recomienda'),
    # path('recomiendaId/<int:movie_id>/', views.recomendadasId, name="recomiendaId")
    path('download_my_csv', views.download_csv),

]