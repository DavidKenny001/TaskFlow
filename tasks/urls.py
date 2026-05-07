from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('tarefas/criar/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/<int:id>/', views.detalhe_tarefa, name='detalhe_tarefa'),
]