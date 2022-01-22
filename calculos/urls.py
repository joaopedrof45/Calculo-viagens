from django.contrib import admin
from django.urls import path 
import calculos.views



urlpatterns = [
    path('', calculos.views.ListarTodosCalculos ,name='listartodos'),
    path('lista-calculos/<str:id>/', calculos.views.ListarCalculoId ,name='listarcalculo'),
    path('cadastrar-viagem/', calculos.views.FazerCalculo,name='cadastrarviagem'),
    path('listar-todos/', calculos.views.ListarTodosCalculos,name='listartodos'),
    path('editar/<str:id>/', calculos.views.EditarId, name='editarid'),
    path('deletar/<str:id>/', calculos.views.DeletarId, name='deletarid'),
     

]
