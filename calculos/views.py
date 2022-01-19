from django.shortcuts import render ,redirect
from .forms import FormCalculo


# Create your views here.



def FazerCalculo(request):
    template_name = 'fazer-calculo.html'


    context ={}
    if request.method =='POST':
    
        form = FormCalculo(request.POST)

        if form.is_valid():
            context['is_valid'] = True
            form.save()
            return redirect('/calculos')

    else:
        form= FormCalculo()
        print("entro no else")


    context['form']=form

    return render(request, template_name, context)


def ListarCalculo(request):
    pass



