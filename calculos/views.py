from django.shortcuts import render ,redirect
from .forms import FormCalculo
from .models import Calculos


# Create your views here.



def FazerCalculo(request):
    template_name = 'fazer-calculo.html'


    context ={}
    if request.method =='POST':
    
        form = FormCalculo(request.POST)

        if form.is_valid():
            context['is_valid'] = True
            context['tittle'] = "Teste"
            form.save()
            return redirect('/calculos')

    else:
        form= FormCalculo()
        print("entro no else")


    context['form']=form

    return render(request, template_name, context)


def ListarCalculoId(request):
    template_name = 'base.html'
    return render(request, template_name)


def ListarTodosCalculos(request):
    List= Calculos.objects.all()
    template_name = 'ListarTodos.html'
    return render(request, template_name ,{'List':List})



