from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurante

#primero vamos a crear un lugar
#primero importamos los modelos creados
#vamos a crear un lugar y luego un restaurante
#------------------------------
#creamos la logica en las vistas, esta vez para verificar usamos un httpresponse
# de forma temporal con el mensaje los datos han sido creados
#la logica dice que la funcion crear debe crear place y restaurante que son los nombres 
# de las clases modelos, entonces crear los detalles que contienen los objetos 
def create(request):
    #creamos una variable con Place(clase) y le pasamos los datos teniendo en cuenta
    #los atributos que contiene la clase Place 
    place = Place(name="Restorant Makabros", addres="Parque Boston")
    #debemos indicarle salvar porque no lo hemos hecho a traves de place.objects
    place.save()
    #ahora para crear el restaurante que tiene un valor con relacion al objeto
    #place, le pasamos el objeto con el que tiene la relacion (place)
    restaurant = Restaurante(place=place, number_of_employees=8, score=5)
    restaurant.save()
    #podemos aprovechar el metodo de respuesta y le cambiamos el mensaje por
    #restaurant.place.name y accedemos al sitio y al nombre
    #return HttpResponse(restaurant.place.name)
    #esta es la forma de acceder al nombre y a la direccion y al numero de empleados
    #se hace con un f string y con el punto se va accediendo a los valores
    return HttpResponse(f"{restaurant.place.name} - {restaurant.place.addres} - {restaurant.number_of_employees} empleados - {restaurant.score} en puntaje")






