from django.shortcuts import render ,redirect , get_object_or_404
from .forms import FormCalculo
from .models import Calculos
from django.core.paginator import Paginator

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


def ListarCalculoId(request,id):
    post = get_object_or_404(Calculos, pk=id)
    template_name = 'EditarCalculo.html'
    
    return render(request, template_name,{'List':post})


def ListarTodosCalculos(request):

    #jogando resultados para paginator

    post_list = Calculos.objects.all().order_by('-numero_protocolo')
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    template_name = 'ListarTodos.html'
    return render(request, template_name ,{'List':posts})


def EditarId(request,id):
    post = get_object_or_404(Calculos, pk=id)
    
    
    form = Calculos(request.POST)
    form.save()

    #nao funciona , se na der para passar a instancia  completa do post para o objeto 
    #pode-se fazer manual instanciando o objeto e passando os atributos individualmente do post do form
    # para dentro do atributo o obejeto
    # exe calculo.valor_passagem= request.POST['valor_passagem']
    #depois dar o objeto.save()


    return redirect('/calculos')
    



def DeletarId(request,id):
    post = get_object_or_404(Calculos, pk=id)
    post.delete()
    return redirect('listartodos')
  





