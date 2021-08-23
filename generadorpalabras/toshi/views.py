from django.shortcuts import render, HttpResponse

def index(request):
    """ return HttpResponse("app de Toshi") """
    return render(request, "toshi/index.html")


def crear(request):
    """ return HttpResponse("crear") """
    return render(request, "toshi/creando.html")


def mostrar(request):
    """ return HttpResponse("mostrando datos") """
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "toshi/mostrando.html", context)


def eliminar(request):
    return HttpResponse("eliminando datos")