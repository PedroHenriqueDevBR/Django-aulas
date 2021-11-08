# Persistindo imagens no Django

Esse diretório armazena um exemplo de como nós podemos fazer a persistencia de imagens no Django.


## Requisitos

1. Django
2. Django Rest Framework
3. Pillow


## Criação do projeto

Primenramente vamos criar um projeto django com os seguintes comandos:

```bash
# Cria o ambiente virtual
virtualenv .venv

# Ativa o ambiente virtual
source .venv/bin/activate

# Instala as depedências necessárias
pip install django djangorestframework pillow

# Cria o projeto
django-admin startproject image_project
cd image_project

# Cria o app core
python manage.py startapp core

```

## Configuração do projeto 

Com o projeto criado, vamos agora para os passos necessários para que o upload de imagens seja aceito na nossa aplicação

### Passos:

**1. Arquivo settings.py**

Vamos acessar as configurações do projeto e incluir as seguintes linhas de código.

***obs:** A maior parte do código de settings foi ocultada do exemplo por não ter necessidade de ser apresentada.*

```python

from pathlib import Path
import os # Importante para que possamos acessar as configurações do sistema operacional onde a aplicação será executada.


BASE_DIR = Path(__file__).resolve().parent.parent # Referencia a base do nosso projeto em relação aos diretórios do sistema

INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'core', # Incluir a aplicação core nas aplicações instaladas
]


STATIC_URL = '/static/'

# Abaixo de STATIC_URL devemos informar para as configurações onde as imagens serão armazenadas em  MEDIA_URL
MEDIA_URL = '/media/'

# MEDIA_ROOT refencia a raiz dos arquivos recebidos
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
...

```

**2. Arquivo urls.py**

O arquivo de urls é importante pois as imagens precisam passar por essa estrutura para que seja enviada para as nossas views.

Então a configuração que nós precisamos fazer nesse arquivo é o seguinte.

```python
...
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# O + static informa para as urls onde as imagens serão armazenadas conforme as constantes informada no arquivo de settings.

```

**3. Modelo Photo**

O modelo informa para o ORM do Django como nós iremos persistir os dados no banco de dados, são as regras que precisam ser seguidas para que as imagens sejam armazenadas.

```python
from django.db import models
import uuid
import os

# Método que será utilizado para formatar o nome das imagens antes de armazenar as mesmas
def upload_image_formater(instance, filename):
    return f"{str(uuid.uuid4())}-{filename}"

# Model que nós iremos utilizar
class Photo(models.Model):
    image = models.ImageField(upload_to=upload_image_formater, blank=True, null=True)

    # verifica se há alguma imagem vinculada ao atributo image
    def has_image(self):
        return self.image != None and self.image != ''

    # Remove a imagem do diretório /media sem deletar Photo
    def remove_image(self):
        if self.has_image():
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        self.image = None

    # Remove a imagen do diretório /media e deleta Photo
    def delete(self):
        if self.has_image():
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete()

```

**3.2 . serializer Photo**

O serializer é opcional porém é interessante para nós desenvolvedores ter essa possibilidade de usar um serializer ao invés de ter que formatar na mão o JSON a ser reecbido e retornado pela aplicação.

```python
from rest_framework.serializers import ModelSerializer
from .models import Photo

'''
O que essa classe vai fazer para nós é basicamente 
pegar o JSON recebido e converter em objetos ou vice-
versa
'''
class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image'] # Esses são os atributos que serão levados em conta na serialização
```

**4. Views**

Agora nós podemos partir para as nossas views, aqui nós iremos criar os métodos para manipular as imagens.

```python

from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response

from core.serializers import PhotoSerializer
from .models import Photo

class ImageView(APIView):
    name = 'image-view'

    # Lista todas as imagens armazenadas
    def get(self, request):
        photos = Photo.objects.all()
        # serializer irá converter os objetos em JSON
        serializer = PhotoSerializer(photos, many=True)
        # serializer irá converter os objetos em JSON
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Adiciona uma nova imagem no banco de dados
    def post(self, request):
        # Acesso aos dados recebitos no request
        data = request.data
        # Acesso ao atributo image especificamente
        image = data['image']
        # Criação de uma nova foto e salvando a image recebida
        photo = Photo.objects.create(image=image)
        # Retorna a imagem serializada para o requester
        serializer = PhotoSerializer(photo, many=False) # many=False pois só há um objeto
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ImageEditView(APIView):
    name = 'image-edit-view'

    # Atualiza a imagem de uma Photo removendo a atual imagem e sanvando uma nova
    def put(self, request, pk):
        try:
            # Pega a instancia de Photo caso ela exista
            photo = Photo.objects.get(pk=pk)
            image = request.data['image']
        except:
            # Caso Photo não seja localizada no banco de dados então um erro é gerado
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Remove a image atual da photo
        photo.remove_image()
        # Adiciona uma nova image
        photo.image = image
        # Salva a alteração
        photo.save()
        # Retorna a nova imagem serializada para o requester
        serializer = PhotoSerializer(photo, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Deleta a imagem do banco de dados e do diretório /media
    def delete(self, request, pk):
        try:
            # Pega a instancia de Photo caso ela exista
            photo = Photo.objects.get(pk=pk)
        except:
            # Caso Photo não seja localizada no banco de dados então um erro é gerado
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Deleta a imagem do banco de dados
        photo.delete()
        # Retorna status 204, pois a imagem não existe mais
        return Response(status=status.HTTP_204_NO_CONTENT)


```
