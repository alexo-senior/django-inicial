"""
URL configuration for firstproyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstproyect import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('primer_saludo/', views.primer_saludo, name = 'primer_saludo'),
    path('despedida/', views.despedida, name ='despedida'),
    path('practica/', views.practica, name ='practica')
]
