from django import forms
#from django.core.exceptions import ValidationError



#aqui definimos las clases que seran los fomularios
#la forma de trabajar con los formularios es parecida 
#a como se trabaja con los modelos
class CommentForm(forms.Form):
    """clase para formulario de comentarios"""
    
    name = forms.CharField(label="Escribe tu nombre", help_text="100 caracteres maximo",max_length=100, )#colocamos un texto de ayuda
    url = forms.URLField(label="Tu sitio web", required=False, initial='http://')
    comment = forms.CharField()
    submit = forms.CharField(widget=forms.widgets.Input(attrs={
        'type':'submit',
        'value':'Enviar',
        'class':'btn btn-primary'
    }))
    
# arriba ejemplo de como se hace el boton en el formulario de django
#en lugar de hacerlo en el template de html

#----------FORMULARIO EN DJANGO PARA DARLE ESTILO CON CSS---------

#formulario de informacion de contacto
#por medio de widget le podemos agregar estilo al formulario
#pero ya en el html, widget.html
#esto es porque ya se le atribye un nobre de clase input
#aqui le aplique la misma regla a todas las casillas, pero puede ser diferente
class ContacForm(forms.Form):
    """clase para formulario de contacto"""
    name = forms.CharField(label="Nombre", max_length=50, 
                        widget=forms.TextInput(attrs={'class':'input'}))
    email = forms.EmailField(label="Email", max_length=50, 
                            widget=forms.EmailInput(attrs={'class':'input'}))
    message = forms.CharField(label="Message", max_length=200, 
                            widget=forms.Textarea(attrs={'class':'input'}))
    
#--------VALIDACIONES DE FORMULARIOS, ES DECIR AGREGAR REGLAS PARA VERIFICAR-------------
#POR EJEMPLO SI SOLO QUEREMOS QUE SEAN EMAIL CORPORATIVOS QUE ASI SEA, LOS 
#DEMAS SEAN RECHAZADOS
#como valido que los datos sean asi como se piden en la clase contacform, nombre, email y mensaje?
#django usa un metodo que se llama ISVALID, creamos un formulario coon este

#----------VALIDACION DE CLEAN_NAME SE HACE EN FORM.PY------
#ESTA VALIDACION SE ´PUEDE HACER ADICIONAL A LAS DEMAS
#HEMOS HECHO, ELE EJEMPLO ES CON LA LONGUITUD DEL NOMBRE.




#EN ESTE EJEMPLO ES VALIDAR SI EL NOMBRE INTRODUCIDO
#ES DIFERENTE DEL ESPERADO

    def clean_name(self):
        """funcion para validar datos segun sea"""
    #funcion para validar que el dato deseado sea correcto
        name = self.cleaned_data.get('name')
        if name != "Alexis":
            raise forms.ValidationError("Solo Alexis esta permitido en este campo")
        else:
            return name
    
    
    
    
    







    
    
    
    
    

    
    
    
    
    
    
    
    
    