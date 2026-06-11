from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task
from .forms import CadastroForm, TarefaForm

def cadastro(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    return render(request, 'tasks/cadastro.html', {'form': form})

@login_required
def dashboard(request):
    tarefas = Task.objects.filter(usuario=request.user)
    prioridade = request.GET.get('prioridade')
    status = request.GET.get('status')
    if prioridade:
        tarefas = tarefas.filter(prioridade=prioridade)
    if status:
        tarefas = tarefas.filter(status=status)
    return render(request, 'tasks/dashboard.html', {'tarefas': tarefas})

@login_required
def criar_tarefa(request):
    form = TarefaForm()
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('dashboard')
    return render(request, 'tasks/criar_tarefa.html', {'form': form})

@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Task, id=id, usuario=request.user)
    form = TarefaForm(instance=tarefa)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'tasks/editar_tarefa.html', {'form': form, 'tarefa': tarefa})

@login_required
def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Task, id=id, usuario=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('dashboard')
    return render(request, 'tasks/confirmar_exclusao.html', {'tarefa': tarefa})

@login_required
def detalhe_tarefa(request, id):
    tarefa = get_object_or_404(Task, id=id, usuario=request.user)
    return render(request, 'tasks/detalhe_tarefa.html', {'tarefa': tarefa})