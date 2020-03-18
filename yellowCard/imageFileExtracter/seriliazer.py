from rest_framework import serializers
from .models import ImageFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = ['id','text',]