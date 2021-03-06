from django.shortcuts import render, HttpResponse

from .models import Jugador

def index(request):
    """ return HttpResponse("app de Toshi") """
    return render(request, "criscuevas/index.html")


def crear(request):
    # request.post['parametro']
    # capturando los parametros enviados por el formulario
    Jugador.objects.create(
    player_name = request.POST['player_name'],
    player_number = request.POST['player_number'],
    player_team = request.POST['player_team']
    )
    return render(request, "criscuevas/crear.html")
