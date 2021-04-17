
from django.contrib import admin
from django.urls import path
from reto1 import views as local_views
from dashboards import views as dashboards_views
from dashboards.homeview import homeview

#hay que regresar una instancia de HttpResponse con el contenido que nosotros queramos
urlpatterns = [
    path('', homeview.home, name = 'home'),
    path('dashboard/', homeview.dashboard, name='Dashboard'),
    path('form/', homeview.form, name = "Formulario"),
]
#al url le hace falta un argumento posicional, que es la vista