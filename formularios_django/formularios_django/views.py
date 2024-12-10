from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContacForm


def form(request):
    #Instancia la clase CommentForm
    #a los comentario se le puede pasar valores si queremos
    #estos coemntarios aparecen ya rellenados en el formulario web
    comment_form = CommentForm()
    #comment_form = CommentForm({'name':'Alexis','url':'http://open-bootcamp.com', 'comment':'comentario'})
    #le pasamos el contexto a la funcion 
    return render(request, 'form.html', {'comment_form':comment_form})
    #return HttpResponse("sitio en construccion")

#----FORMULARIOS DE DJANGO EN VEZ DE HTML A TRAVES DE CLASES----
#las clases herededaran de form y definiran nuestro formulario
#una vez creados los formularios como clase, es decir definimos que 
#debe contener cada uno, se los pasamos coo contexto a nuestro template 
#para que el template lo pinte o renderice

# la vista goal va a estar recepcionando la informacion y gestionando
#la url goal
"""def goal(request):
    if request.method != "GET":
        return HttpResponse("Metodo no permitido")
    return HttpResponse(request.GET['name'])
    return HttpResponse("Recibido")
"""
#-------METODO POST---------------

def goal(request):
    if request.method != "POST":
        return HttpResponse("Metodo no permitido")
    return HttpResponse(request.POST['name'])
    #return HttpResponse("Recibido")
    
    """
    PREGUNTAS QUE PUEDEN SURGIR:
    1:como puedo validar los datos de una forma eficiente
    
    2:como puedo personalizar el contenido mostrado al mismo
    grado que se puede hacer en el formulario html
    
    3:como personalizar las validaciones
    
    4:si quiero hacer un crud sobre un modelo,la estructura
    de un formulario en python es muy similar a la de un modelo,
    existe alguna forma para no tener que duplicar el contenido
    que estoy creando  y de unica vez a partir del modelo se genere
    el formulario, sin tner que escribir desde cero
    """


def widget(request):
    form = ContacForm()
    return render(request,'widget.html', {'form':form} )
    #return HttpResponse("Exito")
    
    




    
    