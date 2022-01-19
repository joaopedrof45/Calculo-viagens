from django.contrib import admin
from django.urls import path 
import calculos.views



urlpatterns = [
    path('', calculos.views.FazerCalculo),
    path('/lista-calculos', calculos.views.ListarCalculo),

]
