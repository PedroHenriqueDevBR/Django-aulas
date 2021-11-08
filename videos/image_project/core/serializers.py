from rest_framework.serializers import ModelSerializer
from core.models import Photo

class PhotoSerializer(ModelSerializer):

    class Meta:
        model = Photo
        fields = ['id', 'image']
