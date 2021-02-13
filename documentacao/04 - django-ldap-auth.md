# Autenticação e utilização do protocolo ldap no Django

## Instalação

### Linux (Debian e derivados)

A utilização do pacote ldap depende do python-ldap, e para que o pacote python-ldap funcione corretamente do Linux, precisamos instalar algumas bibliotecas importantes.
Confira o comando abaixo e faça a instalação dos pacotes necessários.

```bash
// O comando abaixo aplica-se ao SO Debian e derivados
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```


Após fazer a instalação dos pacotes, instale o python-ldap

```bash
python -m pip install python-ldap
```

Agora nós podemos fazer a instalação do pacote que vai ser servir de ponte para que possamos executar comando através do python-ldap.
Portanto instale a seguinte biblioteca.

```bash
pip install django-auth-ldap
```

### Windows (Teste realizado no Windows 10)

Para que o pacote python-ldap possa ser istaaçdo no windows, será necessário que a instalação seja feita por meio dos arquivos binários da biblioteca.

Site contendo os arquivos binários: [https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-ldap](https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-ldap)

Antes de fazer o download do arquivo, verifique qual é a versão do Python isntalado no seu computador, no meu caso a versão é a 3.8.x, como mostra o exemplo abaixo.

```bash
(venv) C:\PedroHenriqueDevBR\Dev\LDAP>python --version                             
> Python 3.8.2
```

Acesse o site descrito acima, procure por python-ldap, após localizar os arquivos observe que há várias versões da bilbioteca, escolha a que está de acordo com a versão do Python instalado no seu computador e escolha a opção de 32 bits independente de qual arquitetura você está utilizando, no meu caso eu baixei o seguinte arquivo.

**python_ldap-3.3.1-cp38-cp38-win32.whl**

Agora faça a instalação do pacote utilizando o seguinte comando:

```bash
pip install --only-binary :all: {python_ldap-3.3.1-cp38-cp38-win32.whl}

# Oberve a opção --only-binary :all:
# Não esqueça de digitar todo o comando
# Troque o que está dentro de {} pela sua versão baixada, o que está sendo apresentado dentro dos colchetes é apenas para exemplo.
```


**Pronto os pacotes necessários para conexão estão disponíveis para utilização.**

## Configuração do projeto no Django

