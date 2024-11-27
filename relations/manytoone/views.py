from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date
#---------------MUCHOS A UNO---------------

#instanciamos las clases de los modelos luego de la funcion

def create(request):
    reportero = Reporter(first_name='Alexis Ibarra', last_name= 'Ibarra Fernandez', email='alexisdemo@gmail.com')
    reportero.save()
    #--------------------------
    #instanciamos la clase Article
    #le colocamos siempre los mismos parametros o columnas de la clase modelo
    #y el ultimo parametro es la clase reporter igual a reportero que tiene los datos
    #todos estos articulos son escritos por el mismo reportero
    articulo1 = Article(headline='este es la noticia del quince',public_date=date(2024,11,15), Reporter=reportero)
    articulo1.save()
    articulo2 = Article(headline='este es la noticia del dieciseis',public_date=date(2024,11,16), Reporter=reportero)
    articulo2.save()
    articulo3 = Article(headline='este es la noticia del diecisiete',public_date=date(2024,11,17), Reporter=reportero)
    articulo3.save()

    #ahora para consultar creamos una variable contendra el numero del articulo mas la clase reporter y para 
    #acceder a la informacion podemos elegir ya sea el nombre , el email etc
    #si quiero acceder a toda la info del reportero hago un f string
    #ya sea un ariculo o muchos si es el mismo autor
    
    consultas = (f"{articulo1.Reporter.first_name} - {articulo2.Reporter.last_name} - {articulo3.Reporter.email}")
    #consultas = reportero.article_set.all()
    
    #----------UNO A MUCHOS-------------------
    #la forma de hacerlo cuando es muchos a uno es al reves pero usando el nombre de la instancia de la clase Reportero set
    #que es reportero.article_set y usar la funcion all()
    #se puede hacer filter
    #consultas2 = reportero.article_set.filter(headline='este es la noticia del diecisiete')
    
    #se puede hacer conteo de articulos
    
    #consultas3 = reportero.article_set.count()
    return HttpResponse(consultas)

    
    
    
    
    

