#usamos render para renderizar los templates
from django.shortcuts import render

#en lugar de devolver una respuesta http, vamos a devolver un template
#es decir un trozo de texto dentro de un archivo, que sera html
#las plantillas van a contener la parte visual del codigo


#explicacion en esta funcion con un parametro de request, va a retornar un render que debe contener
#tres parametros ,un request, el nombre de la plantilla html y el contexto, que es un diccionario,
#en este caso lo pasamos vacio ya que no tenemos un contexto

def simple(request):
    return render(request, 'simple.html', {})

def dinamico(request, name):
    categorias = ['codigo', 'diseño', 'marketing','bussines']
    context = {'name': name, 'categorias':categorias} #se crea una variable con el contexto para darle mas funcionalidad al codigo
    return render(request, 'dinamico.html', context)#tiene los tres parametros; request, nombre plantilla y
                                                    #la variable que contiene el contexto
                                                    

