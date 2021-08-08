
# Create your views here.

from django.shortcuts import render,redirect
from time import localtime, strftime
    
def fechahora(request):
    context = {
        "titulo": "Fecha y hora actual",
        "time" : strftime("%Y-%m-%d %H:%M %p", localtime()),
        
    }
    return render(request,'app1/index.html', context)


def root(request):
    return redirect ("/")


