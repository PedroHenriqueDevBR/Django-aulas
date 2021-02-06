# Django

[Site do Django](https://www.djangoproject.com/)

O Django é um Framework completo, indicado para que deseja criar aplicações web com um nível de segurança maior.

# Observação

Antes de fazer a instalação do Django no computador é importante que os passos de configuração do ambiente de desenvolvimento tenham sido realizados.

# Teoria importante

### Estrutura de um projeto Django

![projeto django](https://studygyaan.com/wp-content/uploads/2019/07/Best-Practice-to-Structure-Django-Project-Directories-and-Files-1024x676.png)

### Arquitetura do django

![Arquitetura django](https://www.ufsm.br/app/uploads/sites/791/2020/09/fb5190cc-2445-450b-a46f-278aa735fd5b-768x905.jpg)


## Instalação

Após a ativação do ambiente virtual no computador ter sido realizada, basta digitar o seguinte comando.

```bash
pip install django

```

Após instalar o Django, podemos executar o seguinte comando para verificar os pacotes instalados no ambiente virtual.

```bash
asgiref==3.3.1
Django==3.1.6
pytz==2021.1
sqlparse==0.4.1

```


## Diferença entre projeto e aplicação

No Django nós criamos um projeto, ou seja, todo o código faz parte de um projeto e esse projeto possui as configurações necessárias para a implantação em um servidor, somente isso não é o suficiente para que tenhamos uma página na web, será necessário a criação de aplicações, ou módulos em um termos mais simples.
Cada aplicação do Django fica responsável por uma serie de finalidades de um escopo definido, isso facilita a manutenção do código e divisão dos arquivos de código fonte.

## Criando um projeto

Para criar um projeto no Django precisamos digitar o seguinte comando.

```bash
django-admin startproject {Nome do projeto}

```

Após a execução do comando acima podemos verificar que uma pasta foi criada com os seguintes arquivos.

```bash
manage.py
├─ {Nome do projeto}
│    ├── asgi.py
│    ├── __init__.py
│    ├── settings.py
│    ├── urls.py
│    └── wsgi.py
```


## Criando uma aplicação

No mesmo diretório do arquivo manage.py, execute o seguinte comando.

```bash
python manage.py startapp {Nome da aplicação}
```

Após a execução do comando acima podemos verificar que uma pasta foi criada com os seguintes arquivos.

```bash
{Nome da aplicação}
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
```

## Entendendo os arquivos de projeto e aplicação.

```bash

# Configurações
__init__.py
manage.py
settings.py
urls.py
wsgi.py
asgi.py

# Aplicação
admin.py
migrations
└── __init__.py
models.py
views.py
```


## Configurando o projeto

* Confingurando o arquivo settings.py
* Criado o primeiro arquivo **.html** (template)
* Criando a primeira função (view)
* Vinculando uma url à view criada.
* Acessando a url no browser


## Models

O Django utiliza um ORM para gerenciar as consultas ao banco de dados, para criar um modelo que possa ser entendido pelo ORM do Django, precisamos ciar uma classe de acordo com as regras do ORM.

Essas regras serão criadas no arquivo models.py, podemos dizer que esse arquivo defini as entidades e os atributos das tabelas no banco de dados.

## Migração das alterações para o banco de dados

Após a criação das entidades no models.py, precisamos informar para o django que ele já pode salvar as alterações no banco de dados, e para que isso seja feito vamos executar dois comandos.

```bash
python manage.py makemigrations

# Esse comando vai criar o arquivo com as alterações realizadas no banco de dados
```

E em seguida

```bash
python manage.py migrate

# Esse comando vai aplicar as alterações no banco de dados.
```

## Sistema de templates do Django (Jinja2)

O Django permite a criação de arquivos **html** formatados antes de ser disponibilizado para o usuário, para que essa funcionalidade possa funcionar, o Django utiliza uma melhoria do Jinja2 que é um formatador de html proprio para o Python que é chamado de DjangoTemplate.

Com o DjangoTemplate podemos aplicar funções dentro de arquivos html antes de ser disponibilizado para o usuário, funções como:

* for 
* if
* else 
* acesso à variáveis
* internacionalização
* etc.

Todas essas funções são delimitadas por blocos escape do DjangoTemplate, ou seja, o que estiver dentro de um bloco conhecido pelo DjangoTemplate o django vai aplicar a função.

## Criação de formulários

Para que um formulário possa ser criado precisamo declarar um bloco dentro da tag **<form>**, para que o Django possa prevenir ataques.

Bloco que deve ser adicionado.

```html
<form>
{% csrf_token %}
...
</form>
```