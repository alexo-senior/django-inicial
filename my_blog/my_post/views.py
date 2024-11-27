from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry
from django.http import HttpResponse

#se importan los modelos Author y Entry 
#esta vez se trabajara con render por lo que la funcion recibe tres parametros
#el render,el nombre de la carpeta y el archivo html y el contexto que esta en blanco por ahora
#-----------------------
#En esta funcion de actualizacion para actualizar se toma o llama el objeto
#mediante get con el id que se necesite, luego se modifica en lo que se necesite
#django no lo tomara como un nuevo objeto sino que sabra que es el mismo objeto modificado

def update(request):
    author = Author.objects.get(id=1)
    author.name = "Alexis Antonio Ibarra F."
    author.email = "iafrpipe@gmail.com"
    author.save()
    #si queremos como prueba podemos devolver una respuesta HTTP
    return HttpResponse("registro modificado con exito")


def queries(request):
    #obtener todos los elementos, ya sea autores o entradas en un objeto
    #creamos un objeto que contenga la busqueda se llama authors
    authors = Author.objects.all()
    #podemos aplicar un filtro a los datos
    #puede ser POR CONDICIONque queramos: y en el contexto igual dict
    filtered = Author.objects.filter(email='alejandra87@example.com')
    #pasamos el contexto en dict ,la clave es authors y el valor es authors es decir el objeto
    #que contiene los valores
    

    
    #como obtener un unico objeto SIN CONDICION(filtrado) 
    #GET solo devuelve un unico valor
    #no olvidar hacer la operacion por el contexto
    
    author = Author.objects.get(id=1)
    
    #obtner los 10 primeros elementos
    # se puede aplicar la funcion all(), y luego se 
    #le coloca un limite como un diccionario [:10]
    limits = Author.objects.all()[:10]
    
    #obtener los diez elementos saltando los cinco primeros (offset)
    #saltando los cinco primeros y extrayendo los cinco siguientes
    offsets = Author.objects.all()[5:10]
    
    #obtener todos los elementos ordenados cmo si fuera order by en sql
    
    orders = Author.objects.all().order_by('email')
    
    #obtener todos los elementos cuyo id sea menor o igual a 15
    #debemos especificar si queremos consultar uno o mas id,añadimos la doble barra baja
    #en el parentesisseguido de lte que significa lower than equal menor o igual que
    #id__=15
    filtereds2 = Author.objects.filter(id__lte=15)
    
    #obtener todos los autores que contienen en su nombre la palabra yes
    filtereds3 = Author.objects.filter(name__contains='yes')
    
    

    return render(request, 'post/queries.html', {'authors':authors, 'filtered':filtered, 'author':author,'limits':limits,'offsets':offsets,'orders':orders,'filtereds2': filtereds2, 'filtereds3':filtereds3})






    












    

# Create your views here.
