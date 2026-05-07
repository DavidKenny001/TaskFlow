from django.shortcuts import render

def dashboard(request):
    return render(request, 'tasks/dashboard.html')

def login_view(request):
    return render(request, 'tasks/login.html')

def cadastro(request):
    return render(request, 'tasks/cadastro.html')

def criar_tarefa(request):
    return render(request, 'tasks/criar_tarefa.html')

def editar_tarefa(request, id):
    return render(request, 'tasks/editar_tarefa.html')

def detalhe_tarefa(request, id):
    return render(request, 'tasks/detalhe_tarefa.html')