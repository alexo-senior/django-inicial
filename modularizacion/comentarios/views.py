from django.shortcuts import render
from django.http import HttpResponse
from .models import Clase_comentario
# importamos la clase_comentario para usarlo en la creacion de un comentario
# Create your views here.
#PRUEBA
#se crea una vista sencilla y se pide una respuesta httpresponse
#para eso primero se importa este tipo de respuesta

def test(request):
    return HttpResponse("Funciona correctamente")

#CREAR UN COMENTARIO:

def create(request):
#creamos un objeto para registar un comentario
# le asignamos la Clase_comentario con sus respectivos parametros que tiene asignado como nombre, score etc
#dejamos la fecha y el signature por defecto
#corremos el servidor y luego miramos en la base de datos y debe estsr reflejado el nuevo comentario
    #un_comentario = Clase_comentario(name = 'Alexis', scoore = 5, comentario = "Este es el primer comentario")
    #de esta forma django guarda el dato
    #un_comentario.save()
    
    # de esta otra forma se crea el comentario y se guarda de forma automatica
    un_comentario = Clase_comentario.objects.create(name = 'Alexis Ibarra', scoore = 10, comentario = "este es el segundo comentario")
    return HttpResponse("ruta para probar la craecion de modelos")

#COMO PODEMOS BORRAR N COMENTARIO:

def delete(request):
    #para borrar primero hay que localizar el objeto a borrar con GET y hacemos casi el mismo proceso
    #el id lo solicitamos porque en la base de datos se va asignando un id automatico por comentario
    #vamos a runserver y luego comprobamos en la base de datos
    
    #un_comentario = Clase_comentario.objects.get(id=1)
    #un_comentario.delete()
    
    #podemos borrar directamente usando los filters instanciando la clase directamente y aplicando delete()
    Clase_comentario.objects.filter(id=2).delete() 
    return HttpResponse("Ruta para probar a borrar un comentario")
















