from django.db import models

#---------------RELACION MUCHOS A MUCHOS-----------------

#un articulo va poder estar en  muchas publicaciones, y una publicacion va
#poder estar en muchos articulos

class Publicacion(models.Model):
    titulo = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.titulo
    
#en esta clase articulo establecemos la relacion con models.manytomanyfield
#solo hace falta hacerlo en una de las clases no en ambas    
class Articulo(models.Model):
    headline = models.CharField(max_length=100)
    #en la relacion esta vez no se define metodo de borrado ya que en la relacion 
    #muchos a muchos se crea en una tabla aparte
    publicaciones = models.ManyToManyField(Publicacion)

    def __str__(self):
        return self.headline
    
    
    
    
    
    