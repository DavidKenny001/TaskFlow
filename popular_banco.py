import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskflow.settings')
django.setup()

from django.contrib.auth.models import User
from tasks.models import Task
from datetime import date

# Criar usuário de teste
if not User.objects.filter(username='teste').exists():
    user = User.objects.create_user(
        username='teste',
        email='teste@taskflow.com',
        password='teste1234'
    )
    print('Usuário criado: teste / teste1234')
else:
    user = User.objects.get(username='teste')
    print('Usuário já existe: teste')

# Criar tarefas de teste
tarefas = [
    {
        'titulo': 'Estudar Django',
        'descricao': 'Revisar models, views e templates',
        'prazo': date(2026, 6, 20),
        'prioridade': 'alta',
        'status': 'pendente',
    },
    {
        'titulo': 'Fazer compras',
        'descricao': 'Comprar itens da lista do mercado',
        'prazo': date(2026, 6, 15),
        'prioridade': 'baixa',
        'status': 'pendente',
    },
    {
        'titulo': 'Reunião de equipe',
        'descricao': 'Reunião às 15h com a equipe do projeto',
        'prazo': date(2026, 6, 16),
        'prioridade': 'media',
        'status': 'concluida',
    },
]

for t in tarefas:
    Task.objects.get_or_create(
        titulo=t['titulo'],
        usuario=user,
        defaults=t
    )
    print(f"Tarefa criada: {t['titulo']}")

print('Banco populado com sucesso!')