
from unicodedata import name
from django.urls import path
from .views import home, crearevento,eventos,modificar,eliminar,registro

urlpatterns = [
    path('', home, name= "home"),
    path('crearevento/', crearevento,name= "crearevento"),
    path('eventos/', eventos,name= "eventos"),
    path('modificar/<id>/',modificar,name="modificar"),
    path('eliminar/<id>/',eliminar,name = "eliminar"),
    path('registro',registro,name= 'registro'),

]
