from django.db import models

# Create your models here.

#cada modelo es una clase
#son los tipos de datos que vamos a estar ultilizando
#cada atributo de la clase sera interpretado a una base de datos sql de forma autmatica
#esto por el uso del orm
#POR CONVENCION DE NOMBRES LOS MODELOS SIEMPRE DEBEN INICIAR CON MASYUSCULA Y EN SINGULAR

class Clase_comentario(models.Model):
    
    name = models.CharField(max_length=255, null=False)
    scoore = models.IntegerField(default=3)
    comentario = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=100, default="firma")
    
    
    
    #definir la cadena str para que devuelva la informacion e el formato
    #que queramos, eso en caso de consultar la informacion 
    def __str__(self):
        return self.name
    
    #las miggraciones se hacen primero con makemigrations para detectar y comenzar a crear
    #la base de datos sql, luego se hace migrate para ejecutar la migracion
    
    
    
    
    
    
    
    

    
    
    
    