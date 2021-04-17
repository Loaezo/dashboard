"""reto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from reto1 import views as local_views
from dashboards import views as dashboards_views
# es python, lo podemos escribir tan mal o tan bien como queramos

#hay que regresar una instancia de HttpResponse con el contenido que nosotros queramos
urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    path('gato/<int:ears>', local_views.gato),
    
    path('dashboards/', dashboards_views.list_dashboards),
]
#al url le hace falta un argumento posicional, que es la vista