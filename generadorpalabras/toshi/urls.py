from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('toshi/', views.index),
    path('toshi/crear/', views.crear),
    path('toshi/mostrar/', views.mostrar),
    path('toshi/eliminar/', views.eliminar),
]