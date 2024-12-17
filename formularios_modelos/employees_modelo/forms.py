from django.forms import ModelForm
from .models import Employees

#la importacion se hace para decirle a django que modelo
#debe utilizar en este caso Employee

"""Esta vez en forms.py no se vuelve a repetir toda la informacion creada en
los model.py sino que se importa de modelform, y se crea una clase con el nombre 
de la clase del modelo añadiendo la palabra Form"""

class EmployeeForm(ModelForm):
    """este modelo hereda de ModelForm, destinado a datos de modelo """
    """aqui le indico a django que tenga los campos necesarios"""
    """se le pasan los campos que va a llevar el formulario"""
    class Meta:
        model = Employees
        #fields = ['name','last_name', 'email']
    #en caso que sea muy extensa la cantidad de campos se usa
        fields = '__all__'
    #para campos extra se añaden los campos
    #extra_fields = ['salary']
    #para excluir solo se colocan los campos a excluir fianliza con la coma
    #    exclude = ('email',)
    
    
    
        
        
        
    
    
        
    """fuera de la clase meta se pueden hacer uso de todas 
    las funcionalidades de un formulario normal, es decir usar 
    las validdaciones con clean, widgets, cualquier de las formas
    para formularios ya que este modelform tiene todas las caract"""
    
    
    
