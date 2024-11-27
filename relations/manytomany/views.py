from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo, Publicacion


#para poder hacer la relcion de muchos a muchos primero se deben guardar los objetos 
#porque para poder re4lacionar los elementos la db debe gusradar los id antes, ya que 
#sino se gusradan los id no existiran pra su relacion

def create(request):
    #primero con los articulos instanciando la clase
    articulo1 = Articulo(headline="articulo primero")
    articulo1.save()
    
    articulo2 = Articulo(headline="articulo primero")
    articulo2.save()
    
    articulo3 = Articulo(headline="articulo primero")
    articulo3.save()
    
    articulo4 = Articulo(headline="articulo primero")
    articulo4.save()
    
    #ahora con las publicaciones nota que se usan los parametos de la clase
    publi1 = Publicacion(titulo="publicacion primera")
    publi1.save()
    
    publi2 = Publicacion(titulo="publicacion primera")
    publi2.save()
    
    publi3 = Publicacion(titulo="publicacion primera")
    publi3.save()
    
    publi4 = Publicacion(titulo="publicacion primera")
    publi4.save()
    
    publi5 = Publicacion(titulo="publicacion primera")
    publi5.save()
    
    publi6 = Publicacion(titulo="publicacion primera")
    publi6.save()
    
    publi7 = Publicacion(titulo="publicacion primera")
    publi7.save()
    #ahora hay que relacionar los artuclos con las publicaciones 
    #y viceversa con el metodo add()
    #estas son relaciones variadas como ejemplo
    
    articulo1.publicaciones.add(publi1)
    articulo1.publicaciones.add(publi2)
    articulo1.publicaciones.add(publi3)
    articulo2.publicaciones.add(publi4)
    articulo2.publicaciones.add(publi5)
    articulo3.publicaciones.add(publi6)
    articulo3.publicaciones.add(publi7)
    
    #una vez hechas las relaciones 
    #hacemos las consultas o busquedas de igual forma que se hace
    
    return HttpResponse("creado con exito") 

 
    
    
    
    
    
    
    
    
    
    

    
