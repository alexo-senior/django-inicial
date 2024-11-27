from django.db import models


class Salary(models.Model):
    amount = models.IntegerField(null=False, blank=False)
    extra_jun = models.BooleanField(default=False)
    extra_dic = models.BooleanField(default=False)
    
    def __str__(self):
        self.amount


class Job(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(null=True)
    #el trabajo tiene una relacion con el salario
    salarys = models.ForeignKey(Salary, on_delete=models.CASCADE)
        
        
    def __str__(self):
        self.title

        
class Country(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    country_code = models.CharField(max_length=6, blank=False, null=False)
    
    def __str__(self):
        self.name
        
    
    
class Location(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    #se relaciona o vincula con el country
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    
    def __str__(self):
        self.name
        
        
                
class Place(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    address = models.CharField(max_length=50,null=False, blank=False)
    zip_code = models.CharField(max_length=5, null=False, blank=False)
    #el place va atener vinculacion con la location
    locations = models.ForeignKey(Location, on_delete=models.CASCADE)
    
        
    def __str__(self):
        self.name
            

#primero creamos las clases con los modelos para cada tipo de control
#se va establecer relaciones de uno a muchos 
#se establecen a traves de claves foraneas             
            
class Employee(models.Model):
    id_number = models.CharField(max_length=10, blank=False, null=False)
    name = models.CharField(max_length=30,blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    #establece la clave foraneas en empleado es con job, el trabajo de esta persona
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    #la relacion con el lugar de trabajo
    places = models.ForeignKey(Place, on_delete=models.CASCADE)
    
    
    def __str__(self):
        self.name    
    