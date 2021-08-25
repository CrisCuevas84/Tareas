from django.shortcuts import render


def index(request):
    return render(request, "form/index.html")


def create_user(request):
    # Imprime mensaje en terminal
    print("Got Post Info....................")
    # Imprime datos en un diccionario en el terminal
    print(request.POST)

    # Creamos variables para obtener los datos de manera individual
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    print(name_from_form)
    print(email_from_form)

    # Se crear contexto para no procesar de inmediato como respuesta a solicictud post
    # Se crea archivo show.html y se agrega al código
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form
    }
    return render(request,"form/show.html",context)
    # return render(request,"form/index.html")
