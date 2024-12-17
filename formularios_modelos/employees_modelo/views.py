from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm


# Create your views here.


def index(request):
    #return HttpResponse("codigo correcto")
    #aqui se crea una instancia de EmployeeForm y se pasa en el contexto
    form = EmployeeForm()
    return render(request, 'index.html', {'form':form})




