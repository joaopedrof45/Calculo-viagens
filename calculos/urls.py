from django.contrib import admin
from django.urls import path 
import calculos.views



urlpatterns = [
    path('', calculos.views.ListarCalculoId ,name='listarcalculo'),
    path('lista-calculos/', calculos.views.ListarCalculoId ,name='listarcalculo'),
    path('cadastrar-viagem/', calculos.views.FazerCalculo,name='cadastrarviagem'),
     path('listar-todos/', calculos.views.ListarTodosCalculos,name='listartodos'),

]
