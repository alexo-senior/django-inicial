from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    short_descritpion = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    #price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()


    
    def __str__(self):
        return self.name
    
    
    
