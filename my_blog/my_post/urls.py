
from django.urls import path
from . import views
#debo importar la vista y asi comunicar a django la ruta de mi vista, asi se controla

#toda aplicacion debe tener su propia url para que sea completa y asi ser mas practico
#al momento de tener que trasladar la app a otro proyecto no trasaldar codigo solo la app

urlpatterns = [
    path('queries/', views.queries, name = 'queries'),
    path('update/',views.update, name ='update')
    
    
]



