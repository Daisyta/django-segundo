
from django.shortcuts import redirect, render, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
#contador = 0

def random(request):
    if 'contador' in request.session:
        request.session['contador'] = request.session['contador'] + 1
    else:
        request.session['contador'] = 1


    context = {
        "palabra" : get_random_string(length=32),
        "contador": request.session['contador'],
        "textolargo": "El nuevo juego de palabras aleatorias",
    }
    return render(request,'random_word/random.html', context)

def random_reset(request):
    request.session['contador'] = 0
    return redirect('/random_word/')