# 🌊 NovaOnda Hotel

Projeto desenvolvido com **Django**, utilizando o NovaOnda Hotel como aplicação prática para construção de uma **base Django organizada, reutilizável e responsiva**.

O projeto está sendo desenvolvido de forma incremental, aplicando conceitos de backend, frontend, banco de dados, templates, Django Admin e Git.

---

## 🎯 Objetivo

Criar uma estrutura Django que possa ser utilizada como base para futuros projetos web, desenvolvendo e testando novas funcionalidades gradualmente.

---

## 🛠️ Tecnologias

### Backend

* 🐍 Python
* 🌐 Django
* 🗄️ SQLite
* Django ORM
* Django Admin

### Frontend

* HTML5
* CSS3
* Bootstrap 5.3.3
* Bootstrap Icons
* JavaScript

### Ferramentas

* Visual Studio Code
* Git
* GitHub
* GitHub Desktop
* Git Bash

---

## 📂 Estrutura

```text
NovaOnda/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
│
├── projeto/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── hotel/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── sobre.html
│   ├── suites.html
│   ├── servicos.html
│   ├── galeria.html
│   ├── contatos.html
│   └── includes/
│
└── static/
    ├── css/
    │   ├── style.css
    │   ├── sobre.css
    │   ├── suites.css
    │   ├── servicos.css
    │   ├── galeria.css
    │   └── contatos.css
    │
    └── imagem/
```

---

## 🧩 Funcionalidades atuais

* 🏠 Página Home
* ℹ️ Página Sobre
* 🛏️ Página de Suítes
* 🛎️ Página de Serviços
* 🖼️ Página Galeria
* 📞 Página Contatos
* 🧭 Menu de navegação responsivo
* 🔽 Dropdown Hotel
* 🗃️ Conteúdo dinâmico através do banco de dados
* 🖼️ Upload e exibição de imagens
* 📝 Formulário de contato
* 💾 Salvamento de contatos no banco
* ⚙️ Gerenciamento através do Django Admin
* 📱 Layout responsivo com Bootstrap

---

## 🗄️ Dados dinâmicos

O projeto utiliza Django ORM para administrar conteúdos como:

* Suítes
* Serviços
* Fotos
* Contatos
* Menu do Hotel
* Café da manhã

Os conteúdos podem ser gerenciados através do **Django Admin**.

---

## 🎨 Identidade visual

O projeto utiliza uma identidade baseada em:

* 🔵 Azul
* 🟡 Dourado
* 🟨 Creme
* ⚪ Branco

O **Bootstrap** é utilizado para estrutura e responsividade, mantendo o CSS personalizado reduzido ao necessário.

---

## 📱 Responsividade

O layout utiliza o sistema de grid do Bootstrap:

```text
Celular  → 1 coluna
Tablet   → 2 colunas
Desktop  → 3 colunas
```

A prioridade é utilizar Bootstrap antes de criar CSS personalizado.

---

## 🧱 Templates

O projeto utiliza herança de templates:

```django
{% extends 'base.html' %}
```

e blocos:

```django
{% block content %}
{% endblock %}
```

Também são utilizados `includes` para componentes reutilizáveis.

---

## ⚙️ Configuração

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar no Git Bash:

```bash
source .venv/Scripts/activate
```

Atualizar pip:

```bash
python -m pip install --upgrade pip
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Aplicar migrations:

```bash
python manage.py migrate
```

Criar administrador:

```bash
python manage.py createsuperuser
```

Executar:

```bash
python manage.py runserver
```

---

## 🧪 Testes

Durante o desenvolvimento são verificados:

* Rotas
* Templates
* Includes
* Bootstrap
* CSS
* Responsividade
* Banco de dados
* Django Admin
* Formulários
* Navegação

---

## 🔮 Próximas etapas

* [ ] Sistema de reservas
* [ ] Página individual das suítes
* [ ] Melhorias na Galeria
* [ ] Autenticação
* [ ] CRUDs
* [ ] APIs
* [ ] Melhorias de segurança
* [ ] Configuração para produção
* [ ] Deploy

---

## 📌 Status

🟢 **Em desenvolvimento**

O NovaOnda Hotel funciona como projeto prático para desenvolvimento e evolução de uma **base Django reutilizável**.

---

## 👨‍💻 Desenvolvimento

Projeto desenvolvido para prática de:

**Python • Django • HTML • CSS • Bootstrap • Banco de Dados • Git • GitHub**
