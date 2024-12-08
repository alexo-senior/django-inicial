
from django.contrib import admin
from django.urls import path
from . import views
#se crea la ruta con el nombre form y los siguientes
#como views.form y el name='form'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/form/', views.getform, name='form'),
    path('get/goal/', views.getgoal, name='goal'),
    path('post/form', views.postform, name="postform"),
    path('postgoal/form', views.postgoal,name="postgoal")
    
]


