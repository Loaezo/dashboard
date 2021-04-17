"""
Vistas del proyecto
"""
#django
from django.http import HttpResponse
import pdb
#utilities

from datetime import datetime


import json

#siempre recibe un request, el objeto del request y regresa una respuesta, pero no tenemos que escribir la respuesta a mano
#para escribir una respuesta http tenemos que importar una herramienta de Django: HttpResponse
def hello_world(request): 
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current time is {now} Don\'t be naco'.format(now=str(now)))

def sort_integers(request):
    """return a JSON response with sorted integers"""
    #numbers_str = request.GET['numbers']
    #numbers = sorted(numbers_str.split(','))
    #numbers_int = int(i) for i in numbers_str
    numbers = [int (i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)

    #pdb.set_trace()

    data = {
        'status'  : 'ok',
        'numbers' : sorted_ints,
        'message' : 'Integers successfully sorted'
    }
    
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hola {}! Welcome to my page!'.format(name)
    return HttpResponse(message)

def gato(response, ears):
    if ears <= 2:
        cabeza = 1
    else:
        cabeza = 0
    return HttpResponse('Usté tiene {} cabezas. Mu bié'.format(cabeza))