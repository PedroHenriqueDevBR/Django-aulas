# Flask - micro-framework

[Site do flask](https://flask.palletsprojects.com/en/1.1.x/)

O Flask é um framework Python com o foco em ser simples, ou seja, esse framework irá disponibilizar é um conjunto ferramentas simples para que você desenvolvedor possa ir evoluindo de acordo com as suas necessidades.

# Importante

Finalize a configuração do ambiente de desenvolvimento no seu computador, siga os passos de configuração apresentado anteriormente.

## Instalação do Flask

O Flask pode ser instalado por meio do **pip**, execute o seguinte comando para instalar o Flask.

```
# Instalação
> pip install flask

# Verifique os pacotes instalados junto com o Flask
> pip freeze

# Exemplo de resposta
click==7.1.2		-> Útil para aplicações e testes no terminal
Flask==1.1.2		-> (X) Pacote do Flask
itsdangerous==1.1.0	-> Aplica criptografia a um dado
Jinja2==2.11.3		-> (X) Gerenciador de templates
MarkupSafe==1.1.1	-> Escape de caracteres especiais em HTML
Werkzeug==1.0.1		-> Utilitários para o WSGI

```


## Criando a primeira aplicação Flask

Hello world!

```python
from flask import (Flask, render_template)

app = Flask('App')

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

```


## @Decorators

Os decorators são métodos que são executados antes da função principal., portanto quando declaramos uma função com o decorator @app.route('/'), isso quer dizer que, antes da nossa função ser executada, o Flask vai vincular a rota '/' com a função hello_world, sendo assim a função hello_word vai ser executada somente após a definição da rota.

## if __name__ == '__main__'

Equivale à função main de outras linguagens, se esse arquivo for executado ao invés de importado, a primeira instrução que será chamada será a **if __name__ == '__main__'**

