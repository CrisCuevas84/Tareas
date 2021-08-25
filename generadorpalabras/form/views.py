from django.shortcuts import render


def index(request):
    return render(request, "form/index.html")


def create_user(request):
    print("Got Post Info....................")
    print(request.POST)
    return render(request,"form/index.html")
