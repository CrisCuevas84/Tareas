from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime

# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request, 'time_display/index.html', context)
