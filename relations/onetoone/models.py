from django.db import models

#----------------RELACION UNO A UNO -----------------------------

#se crea la clase place para el sitio del restaurante con su nombre 
#y la direccion
class Place(models.Model):
    name = models.CharField(max_length=50)
    addres = models.CharField(max_length=80)
    
    #su respectivo str para acceder a la informacion
    def __str__(self):
        return self.name
    
    #se crea la clase restaurante el cual tendra la variable place la cual django asociara a 
    #la app onetoone con el campo o Field, los parametros seran siempre de asociar la clase restaurante 
    #con la clase place para que tengan la conexion siempre que se busque el restaurante se pueda acceder al sitio
    #se usa on_delete en cascada para mantener la intregridad de la base de datos en caso de borrado,y como 
    #ercer parametro una clave primaria para acceder en true
class Restaurante(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    number_of_employees = models.IntegerField(default=1)
    score = models.IntegerField(default=5)
    
    
    #en esta parte pedimos el retorno de el sitio y el nombre del sitio cuando se acceda al restaurante
    #igual que se pide el nombre se pueden pedir otros datos
    def __str__(self):
        return self.Place.name
    
    
    
    
    
    
    
    
    
    
    
    
    