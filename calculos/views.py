from django.shortcuts import render ,redirect , get_object_or_404
from .forms import FormCalculo
from .models import Calculos
from django.core.paginator import Paginator
from django.contrib import messages


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
            messages.success(request,"Viagem Cadastrada com Sucesso")
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

    #se o usuario desejar fazer pesquisa personalizada
    pesquisa = request.GET.get('search')
    opcao = request.GET.get('tipo')
    

    #verificando por qual campo irá fazer o filtro
    if pesquisa:
        if opcao == "numero_protocolo":
            posts = Calculos.objects.filter(numero_protocolo=pesquisa)

        if opcao == "dias_utei":
            posts = Calculos.objects.filter(dias_utei=pesquisa)

        if opcao == "data_inical":
            posts = Calculos.objects.filter(data_inical=pesquisa)

        if opcao == "data_final":
            posts = Calculos.objects.filter(data_final=pesquisa)

        if opcao == "valor_passagem":
            posts = Calculos.objects.filter(valor_passagem=pesquisa)

        if opcao == "valor_translado":
            posts = Calculos.objects.filter(valor_translado=pesquisa)

        if opcao == "cargo":
            posts = Calculos.objects.filter(cargo=pesquisa)

        if opcao == "estado":
            posts = Calculos.objects.filter(estado=pesquisa)

        if opcao == "cidade":
            posts = Calculos.objects.filter(cidade=pesquisa)

        if opcao == "update_at":
            posts = Calculos.objects.filter(update_at=pesquisa)
        
        
    
    template_name = 'ListarTodos.html'
    return render(request, template_name ,{'List':posts})


def EditarId(request,id):

    if request.method =='POST':
        
        post = get_object_or_404(Calculos, numero_protocolo=id)
        
        calculo = Calculos()

        #verificar como arrumar se nao vir o checkbox do defensor que seria 0 ou 1 false ou true , mas 
        #quando desmarcado vem sem nada   

        #nao funciona , se na der para passar a instancia  completa do post para o objeto 
        #pode-se fazer manual instanciando o objeto e passando os atributos individualmente do post do form como
        #mostrado abaixo fazendo request.POST['campo'] ou pelo get_object objeto.atributo

        calculo.defensorbool= post.defensorbool
        calculo.numero_protocolo =id
        calculo.dias_utei=request.POST['dias_utei']
        calculo.data_inical = request.POST['data_inical']
        calculo.data_final=request.POST['data_final']
        calculo.valor_passagem = request.POST['valor_passagem']
        calculo.valor_translado=request.POST['valor_translado']
        calculo.cargo = request.POST['cargo']
        calculo.estado=request.POST['estado']
        calculo.cidade=request.POST['cidade']
        calculo.save()
        messages.success(request,"Viagem Editada com Sucesso")

    return redirect('/calculos')
    



def DeletarId(request,id):
    post = get_object_or_404(Calculos, pk=id)
    post.delete()
    messages.success(request,"Viagem deletada com Sucesso")
    return redirect('listartodos')
  





