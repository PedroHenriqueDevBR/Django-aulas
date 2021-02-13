# Autenticação e utilização do protocolo ldap no Django

## Instalação

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

Pronto os pacotes necessários para conexão estão disponíveis para utilização.

## Configuração do projeto no Django

