from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response

from core.serializers import PhotoSerializer
from .models import Photo

# Create your views here.
class ImageView(APIView):
    name = 'image-view'

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        image = data['image']
        photo = Photo.objects.create(image=image)
        serializer = PhotoSerializer(photo, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ImageEditView(APIView):
    name = 'image-edit-view'

    def put(self, request, pk):
        try:
            photo = Photo.objects.get(pk=pk)
            image = request.data['image']
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        photo.remove_image()
        photo.image = image
        photo.save()
        serializer = PhotoSerializer(photo, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            photo = Photo.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
