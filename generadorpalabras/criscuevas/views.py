from django.shortcuts import render, HttpResponse

def index(request):
    """ return HttpResponse("app de Toshi") """
    return render(request, "criscuevas/index.html")
