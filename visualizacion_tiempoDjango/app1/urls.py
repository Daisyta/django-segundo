from django.urls import path
from . import views

"""    los parametros no fijos se configuran aqui,por ej,de la ruta vacia quiero que me lleve a /1 
o a /2 edsde aca lo puedo hacer,pueden ser numeros,palabras,string (dejar una variable en medio de
las rutas,estos parametros en views van al lado del request dem),"""

urlpatterns = [
    path('', views.fechahora),

]
