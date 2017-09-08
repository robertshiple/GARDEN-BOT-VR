from rest_framework import serializers
from .models import ThreeD

class ThreeDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThreeD
        fields = ('thumb', 'uploaded', 'name', 'type')