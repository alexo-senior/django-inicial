from django.shortcuts import render
from django.http import  HttpResponse

#--------------FORMULARIO GET----------------
#se define la funcion y con request como parametro
#se importa de shortcuts render para renderizar las
#respuestas, como vimos anteriormente el render pide tres
#parametros:request,archivo.html y el contexto
def getform(request):
    return render(request, 'form.html', {})


#creamos la vista de la ruta goal
#esta vista recibe la informacion y devuelve la respuesta
#a success.html con el mensaje
def getgoal(request):
#para gestionar el metodo de forma correcta
    if request.method != 'GET':
        return HttpResponse("el metodo solicitado no esta soportado por la ruta")
#de esta forma se crea un objeto para acceder al nombre del formulario
#y se agrega como contexto de la funcion, asi devuelve el nombre en el success
#por lo que se modifica tambien en elformulario de contacto    
    name = request.GET['name']    
    return render(request,'success.html',{'name':name})

#esta vista maneja las soslicitudes http a la ruta asociada (/post/form)
#renderiza la plantilla postform.html, muestra un formulario post
def postform(request):
    return render(request, 'postform.html', {})


#esta vista maneja las solicitudes http asociada a la ruta (/postgoal/form)
#renderiza la plantilla postform.html
def postgoal(request):
    if request.method == 'POST':
        
        return render(request,'postsuccess.html', {})
    else:
        return HttpResponse("El metodo no esta soportado en la ruta")
    


    



    