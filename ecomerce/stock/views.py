from django.shortcuts import render
from .forms import ProductForm


# Create your views here.

"""def index(request):
    if request.method == 'POST':
        #si es post se crea un formulario con los datos enviados
        form = ProductForm(request.POST)
        #si es valido se guarda
        if form.is_valid():
            form.save()
            #podemos devolver cuando es valido un mensaje de exito
            return render(request, 'index.html', {'form': form})
    else:#podemos hacer un else ya que si no es post es get
        form = ProductForm()
        return render(request, 'index.html', {'form': form})"""
        
from django.shortcuts import render
from .forms import ProductForm

def index(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir o mostrar un mensaje de éxito
            return render(request, 'index.html', {'form': ProductForm(), 'success': 'Producto guardado exitosamente'})
        else:
            # Si el formulario no es válido
            return render(request, 'index.html', {'form': form})
    else:
        # Solicitud GET: formulario vacío
        form = ProductForm()
        return render(request, 'index.html', {'form': form})
    




