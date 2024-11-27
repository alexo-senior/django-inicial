#las vistas contienen la logica con las funciones y las urls asociadas a las funciones
#las vistas siempre reciben un primer parametro que es request
from django.http import HttpResponse

# la siguiente logica devuelve un mensaje
def primer_saludo(request):
    return HttpResponse("Hola familia mundial")

def despedida(request):
    return HttpResponse("Hasta luego familia mundial")

def practica(request):
    return HttpResponse("la practica hace al maestro")





    
    
