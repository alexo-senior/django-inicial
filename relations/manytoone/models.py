from django.db import models

# Create your models here.
#para realizar la vinculacion de uno a muchos es por medio de la
#clave foranea,igual con muchos a uno
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    
    def __str__(self):
        return self.email
    
#ahora para vincular los articulos 

#el elemento que solo puede tener uno del otro es el  que tiene la clave foranea
#es decir como un articulo solo puede tener un reportero este debe tener la clave declarada

class Article(models.Model):
    headline = models.CharField(max_length=100)   
    public_date = models.DateField()
    #respetamos la convencio y reporter lo colocamos igual asociado a la clave foranea
    #el parametro interno debe ser el asociado que es reporter mas el borrado en cascada
    Reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    #en el retorno se pide el headline que es que identifica a que reportero lo hizo
    def __str__(self):
        return self.headline
    
    
    
    
    
    
    
    


    
    