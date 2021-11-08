from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from core.serializers import PhotoSerializer
from core.models import Photo

# Create your views here.
class PhotoListCreateView(APIView):
    name = 'photo_list_create_view'

    # Lista todas as imagens
    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Adiciona nova imagem
    def post(self, request):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class PhotoEditDeleteView(APIView):
    name = 'photo_edit_delete_view'

    # Modificar imagem
    def put(self, request, pk):
        try:
            photo = Photo.objects.get(pk=pk)
            data = request.data
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        photo.remove_image()
        photo.image = data['image']
        photo.save()
        serializer = PhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    # Deletar imagem
    def delete(self, request, pk):
        try:
            photo = Photo.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
