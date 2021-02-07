# DjangoTemplates

O Django possui uma facilidade para a criação de templates, pois o projeto Django utiliza um formatador baseado no Jinja2 como base para a criação de templates .html, nesse tópico vou abordar como nós podemos utilizar esse sistema que facilita na hora de desenvolver aplicações web mais robustas.

[documentação do sistema de templates do django](https://docs.djangoproject.com/en/3.1/ref/templates/language/)

## Estilizando a aplicação 

Para que a nossa aplicação possa utilizar um arquivo css, javascript ou qualquer arquivo estático, precisamos criar um dirtetório com o nome de static em uma aplicação, ou então definir no arquivo settings.py o diretório onde os arquivos estáticos serão localizados.

Aṕos criar o diretório static e dentro do diretório static criar uma pasta css, você pode utilizar esses arquivos estáticos dentro do template html.

Para importar um arquivo estático dentro do template html utilize o seguinte código.

```html
{% load static %}

<!DOCTYPE html>
<html lang="pt-br">

<head>
    ...
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>

<body>
    ...
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
</body>

</html>

```

E a estrututa da aplicação fica da seguinte forma.

```bash
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   ├── __init__.py
│   └── __pycache__
│       └── __init__.cpython-36.pyc
├── models.py
├── __pycache__
│   ├── admin.cpython-36.pyc
│   ├── __init__.cpython-36.pyc
│   ├── models.cpython-36.pyc
│   └── views.cpython-36.pyc
├── static # Diretório com os arquivos estáticos
│   ├── css
│   │   ├── bootstrap.min.css
│   │   └── style.css
│   └── js
│       ├── bootstrap.bundle.min.js
│       └── jquery.min.js
├── templates # Diretório com os templates da aplicação
│   └── index.html
├── tests.py
└── views.py

```

Esse mesmo conceito pode ser utilizado para utilizar imagens ou vídeos no template html.
