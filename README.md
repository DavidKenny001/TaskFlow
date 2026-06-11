# TaskFlow — Sistema de Gerenciamento de Tarefas

## Descrição
O TaskFlow é um sistema web para gerenciar tarefas pessoais, permitindo ao usuário criar, organizar, priorizar e acompanhar suas atividades do dia a dia de forma simples e intuitiva.

## Problema que resolve
A dificuldade de manter o controle de tarefas e compromissos sem uma ferramenta adequada, o que frequentemente leva ao esquecimento de atividades importantes, falta de priorização e baixa produtividade.

## Tipos de usuários
- **Administrador:** acessa o painel Django Admin e gerencia todos os usuários e tarefas do sistema.
- **Usuário comum:** cria e gerencia apenas suas próprias tarefas.

## O que cada usuário pode fazer
- **Administrador:** acessar `/admin/`, gerenciar usuários e tarefas de todos.
- **Usuário comum:** cadastrar-se, fazer login, criar, editar, visualizar e excluir suas tarefas, além de filtrar por prioridade e status.

---

## Instalação e execução

### Pré-requisitos
- Python 3.10+
- Git

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/TaskFlow.git
cd TaskFlow
```

**2. Crie e ative o ambiente virtual:**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Aplique as migrations:**
```bash
python manage.py migrate
```

**5. Popule o banco com dados de teste:**
```bash
python popular_banco.py
```

**6. Inicie o servidor:**
```bash
python manage.py runserver
```

**7. Acesse no navegador:**

http://127.0.0.1:8000/

---

## Dados de teste
Após rodar o script `popular_banco.py`, use as credenciais abaixo para acessar o sistema:

| Tipo | Usuário | Senha |
|---|---|---|
| Usuário comum | teste | teste1234 |

---

## Principais funcionalidades
- Cadastro e login de usuários
- Criar, editar e excluir tarefas
- Definir título, descrição, prazo e prioridade
- Marcar tarefas como concluídas ou pendentes
- Filtrar tarefas por status e prioridade

---

## Painel Administrativo
Para acessar o painel admin crie um superusuário:
```bash
python manage.py createsuperuser
```
Depois acesse `http://127.0.0.1:8000/admin/`

---

## Tecnologias utilizadas
- Python 3
- Django 6
- HTML5 / CSS3
- JavaScript
- SQLite
- Git e GitHub