from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    request.session['intentos'] = 0
    unique_id = get_random_string(length=14)
    context = {
            'unique_id':unique_id,
    } 
    return render(request, 'index.html', context)

def generar(request):
	request.session['intentos'] = 0
	return render(request, 'index.html')

