
from django.contrib import admin
from django.urls import path
from . import views
#se crea la ruta con el nombre form y los siguientes
#como views.form y el name='form'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.form, name='form'),
    path('goal/', views.goal, name='goal')
    
]
