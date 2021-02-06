from functools import wraps


def decorar(f):
    @wraps(f)
    def decorada(*args, **kwargs):
        print('Antes de executar')
        print(f.__name__)
        print('Depois de executar')

    return decorada


def teste():
    print('Olha só que louco')


def teste2():
    resposta = decorar(teste)
    print(resposta.__name__)


if __name__ == '__main__':
    teste2()
