from rest_framework import serializers
from .models import Image   #importe le modèle Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'timestamp']