from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("prueba de que la app funciona")