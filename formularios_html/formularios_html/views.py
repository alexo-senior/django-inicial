from django.shortcuts import render
from django.http import  HttpResponse


#se define la funcion y con request como parametro
#se importa de shortcuts render para renderizar las
#respuestas, como vimos anteriormente el render pide tres
#parametros:request,archivo.html y el contexto
def form(request):
    return render(request, 'form.html', {})

#creamos la vista de la ruta goal
#esta vista recibe la informacion y devuelve la respuesta
#a success.html con el mensaje
def goal(request):
#para gestionar el metodo de forma correcta
    if request.method != 'GET':
        return HttpResponse("el metodo solicitado no esta soportado por la ruta")
#de esta forma se crea un objeto para acceder al nombre del formulario
#y se agrega como contexto de la funcion, asi devuelve el nombre en el success
#por lo que se modifica tambien en elformulario de contacto    
    name = request.GET['name']    
    return render(request,'success.html',{'name':name})
    
    

    