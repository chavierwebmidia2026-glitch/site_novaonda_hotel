# 🚀 Projeto Base Django

Projeto desenvolvido com o objetivo de criar uma **base Django reutilizável, organizada e preparada para evolução**, servindo como ponto de partida para novos projetos web.

A proposta é desenvolver o projeto gradualmente, começando pela configuração fundamental do Django, passando pela criação das páginas, templates, rotas e estilização, e posteriormente adicionando novas funcionalidades conforme a necessidade do projeto.

---

## 🎯 Objetivo do Projeto

Este projeto está sendo desenvolvido como um **projeto-base para aplicações web com Django**.

A ideia é construir uma estrutura organizada que possa ser expandida com:

* Novas páginas
* Novos aplicativos Django
* Banco de dados
* Formulários
* Sistema de autenticação
* Área administrativa
* APIs
* Integração com serviços externos
* Sistema de usuários
* CRUDs
* Painéis administrativos
* Responsividade
* Melhorias de UI/UX
* Deploy em produção

O projeto está sendo desenvolvido de maneira incremental, permitindo testar cada etapa antes de avançar para a próxima.

---

# 🛠️ Tecnologias

## Backend

* 🐍 Python
* 🌐 Django

## Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

## Ferramentas

* Visual Studio Code
* Git
* GitHub
* GitHub Desktop
* Terminal / Git Bash

---

# 📚 Etapas do Desenvolvimento

## 1. Criação do ambiente virtual

Foi criado um ambiente virtual Python para manter as dependências do projeto isoladas.

```bash
python -m venv .venv
```

Ativação do ambiente:

```bash
source .venv/Scripts/activate
```

No Windows, utilizando Git Bash.

---

## 2. Atualização do pip

Após ativar o ambiente virtual, foi realizada a atualização do gerenciador de pacotes:

```bash
python -m pip install --upgrade pip
```

---

## 3. Instalação do Django

O Django foi instalado dentro do ambiente virtual do projeto.

```bash
pip install django
```

---

## 4. Criação do projeto Django

Foi criada a estrutura inicial do projeto Django, estabelecendo a base para o desenvolvimento da aplicação.

A estrutura inicial do Django fornece arquivos responsáveis por:

* Configurações
* URLs
* ASGI
* WSGI
* Gerenciamento do projeto
* Aplicações Django

---

# 📂 Organização do Projeto

A estrutura está sendo organizada para separar responsabilidades e facilitar futuras expansões.

Exemplo de organização:

```text
projeto/
│
├── .venv/
│
├── projeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   └── includes/
│
├── static/
│
├── manage.py
├── requirements.txt
└── README.md
```

A estrutura poderá crescer conforme novas funcionalidades forem adicionadas.

---

# 🧩 Templates

Uma das etapas importantes do projeto foi a criação de uma estrutura de templates reutilizáveis.

A utilização de um `base.html` permite criar uma estrutura principal para o site.

Exemplo:

```text
templates/
│
├── base.html
│
├── home/
│
├── contato/
│
└── includes/
    ├── header.html
    ├── nav.html
    ├── footer.html
    └── card.html
```

Isso permite evitar a repetição de código HTML em todas as páginas.

---

# 🔗 Herança de Templates

O projeto utiliza a herança de templates do Django.

A ideia é possuir uma estrutura principal:

```text
base.html
```

e permitir que outras páginas utilizem essa estrutura.

Exemplo:

```django
{% extends 'base.html' %}

{% block content %}

<!-- Conteúdo da página -->

{% endblock %}
```

Dessa maneira, elementos comuns podem permanecer centralizados no template base.

---

# 🧱 Includes

Também está sendo utilizada a funcionalidade de `include` do Django.

Exemplo:

```django
{% include 'includes/header.html' %}
{% include 'includes/nav.html' %}

{% block content %}
{% endblock %}

{% include 'includes/footer.html' %}
```

Essa organização permite reutilizar componentes como:

* Header
* Navbar
* Footer
* Cards
* Outros componentes futuros

---

# 🛣️ Sistema de Rotas

As URLs estão sendo organizadas através do sistema de rotas do Django.

Exemplo:

```python
path('', views.home, name='home')
```

As rotas permitem conectar:

```text
URL
 ↓
View
 ↓
Template
 ↓
Página exibida no navegador
```

A estrutura está sendo preparada para receber novas páginas e funcionalidades.

---

# 📄 Páginas

O desenvolvimento das páginas está sendo feito gradualmente.

Entre as páginas e componentes trabalhados estão:

* Página inicial
* Header
* Navegação
* Footer
* Componentes reutilizáveis
* Página de contato
* Outras páginas que serão adicionadas durante a evolução do projeto

A página de contato faz parte da próxima etapa de expansão da aplicação.

---

# 🎨 Estilização

A interface está sendo desenvolvida utilizando:

* HTML5
* CSS3
* Bootstrap
* JavaScript

A estilização está sendo trabalhada de forma progressiva.

O objetivo é inicialmente estabelecer uma interface funcional e posteriormente melhorar:

* Layout
* Espaçamento
* Tipografia
* Cores
* Responsividade
* Componentes
* Navegação
* Experiência do usuário
* Identidade visual

---

# 🧪 Testes Durante o Desenvolvimento

Durante o desenvolvimento, cada etapa é testada no navegador utilizando o servidor de desenvolvimento do Django.

```bash
python manage.py runserver
```

O servidor disponibiliza a aplicação localmente para verificar:

* Funcionamento das páginas
* Rotas
* Templates
* Includes
* CSS
* JavaScript
* Navegação

A ideia é corrigir cada etapa antes de avançar para a próxima.

---

# 📦 Controle de Versão

O projeto utiliza Git para controle de versão.

O GitHub Desktop está sendo utilizado para organizar os commits e acompanhar a evolução do projeto.

Os commits seguem uma organização contendo:

### Summary

Uma descrição curta da alteração.

### Description

Uma descrição detalhada utilizando itens:

```text
- Alteração realizada
- Arquivo ou estrutura modificada
- Funcionalidade adicionada
- Testes realizados
- Correções efetuadas
```

Dessa forma, o histórico do projeto funciona também como documentação da evolução da aplicação.

---

# 📈 Estratégia de Escalabilidade

O projeto está sendo desenvolvido pensando na possibilidade de crescimento.

A estrutura inicial foi organizada para permitir a inclusão gradual de novas funcionalidades sem precisar reconstruir toda a aplicação.

A evolução planejada pode seguir aproximadamente esta direção:

```text
PROJETO BASE
     │
     ├── Templates
     │
     ├── Includes
     │
     ├── Rotas
     │
     ├── Views
     │
     ├── CSS
     │
     ├── JavaScript
     │
     ├── Models
     │
     ├── Banco de Dados
     │
     ├── Formulários
     │
     ├── Autenticação
     │
     ├── CRUD
     │
     ├── APIs
     │
     └── Deploy
```

---

# 🔮 Próximas Etapas

O projeto continuará sendo desenvolvido progressivamente.

### Próxima etapa

* Continuar as páginas do projeto
* Finalizar a página de contato
* Ajustar as rotas
* Testar todas as navegações
* Continuar a estilização visual
* Melhorar o layout
* Organizar os componentes

### Etapas futuras

* Criar Models
* Configurar banco de dados
* Criar formulários
* Implementar CRUD
* Criar autenticação
* Criar sistema de usuários
* Trabalhar com Django Admin
* Criar APIs
* Integrar APIs externas
* Melhorar segurança
* Configurar variáveis de ambiente
* Criar arquivo `requirements.txt`
* Preparar o projeto para produção
* Realizar deploy

---

# 🏗️ Visão de Longo Prazo

O objetivo final é transformar esta estrutura em uma **base Django reutilizável**, que possa ser utilizada como ponto inicial para diferentes tipos de projetos.

A ideia é evitar começar todos os projetos do zero.

Uma nova aplicação poderá partir dessa estrutura e receber apenas as funcionalidades específicas necessárias.

```text
                    PROJETO BASE DJANGO
                            │
             ┌──────────────┼──────────────┐
             │              │              │
          FRONTEND       BACKEND        BANCO
             │              │              │
          HTML/CSS       Django         Models
          Bootstrap      Views          Migrations
          JavaScript     URLs           Database
             │              │              │
             └──────────────┼──────────────┘
                            │
                     FUNCIONALIDADES
                            │
              ┌─────────────┼─────────────┐
              │             │             │
            CRUD       AUTENTICAÇÃO      API
              │             │             │
              └─────────────┼─────────────┘
                            │
                          DEPLOY
                            │
                         PRODUÇÃO
```

---

# 📌 Status do Projeto

🟢 **Em desenvolvimento**

A estrutura inicial está sendo construída e testada gradualmente.

O projeto continuará recebendo novas páginas, componentes, rotas, estilos e funcionalidades conforme o desenvolvimento avançar.

---

# 👨‍💻 Desenvolvimento

Projeto desenvolvido para estudo, prática e criação de uma **base reutilizável de projetos Django**.

A documentação será atualizada conforme novas etapas forem concluídas.
