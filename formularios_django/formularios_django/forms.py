from django import forms

#aqui definimos las clases que seran los fomularios
#la forma de trabajar con los formularios es parecida 
#a como se trabaja con los modelos
class CommentForm(forms.Form):
    
    name = forms.CharField(label="Escribe tu nombre", help_text="100 caracteres maximo",max_length=100, )#colocamos un texto de ayuda
    url = forms.URLField(label="Tu sitio web", required=False, initial='http://')
    comment = forms.CharField()
    
    
    
    
    
    
    