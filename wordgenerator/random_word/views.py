from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    unique_id = get_random_string(length=14)

    context = {
            'unique_id':unique_id,
    } 

    return render(request, 'index.html', context)

