from django.db import models
from datetime import date

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    
    def  __str__(self):
        return self.name # devuelve el nombre del author cuando se le solicite
    
    
class Entry(models.Model):
    # para relacionar o referenciar una tabla  o clase con otra se crea la variable author y se se le coloca como clave foranea
    #haciendo referencia a la clase Author que contiene la informacion
    #de esta forma  en author vamos a guardar la clave foranea del Author de la entrada
    #usamos el metodo on_delete= CASCADE para eiminar las entradas del author y conservar la integridad de la base de datos
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    head_line = models.CharField(max_length=255)
    body_text = models.TextField()
    public_date = models.DateField(default=date.today) #importamos la libreria de fecha por datetime
    rating = models.IntegerField(default=5) #este dato sera un entero
    
    #le hacemos su propio str
    
    def __str__ (self):
        return self.head_line #que devuelva el titulo cuando se le solicite
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
