from django import forms

#aqui definimos las clases que seran los fomularios
#la forma de trabajar con los formularios es parecida 
#a como se trabaja con los modelos
class CommentForm(forms.Form):
    
    name = forms.CharField(label="Escribe tu nombre", help_text="100 caracteres maximo",max_length=100, )#colocamos un texto de ayuda
    url = forms.URLField(label="Tu sitio web", required=False, initial='http://')
    comment = forms.CharField()
    submit = forms.CharField(widget=forms.widgets.Input(attrs={
        'type':'submit',
        'value':'Enviar',
        'class':'btn btn-primary'
    }))
    
#ejemplo de como se hace el boton en el formulario de django
#en lugar de hacerlo en el template de html
    
    

class ContacForm(forms.Form):
    name = forms.CharField(label="Nmbre",max_length=50)
    email = forms.EmailField(label="Email",max_length=50)
    message = forms.CharField(label="Message")
    
    
    
    
    
    
    