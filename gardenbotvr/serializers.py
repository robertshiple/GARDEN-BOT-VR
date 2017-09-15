from rest_framework import serializers
from .models import Asset, Scene, Entity


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ('file', 'thumb', 'uploaded', 'name', 'is_moving', 'fchord', 'bchord', 'dchord')


class EntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entity
        fields = ('file', 'thumb', 'uploaded', 'name')


class SceneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scene
        fields = ('name', 'groundcolor', 'skycolor', 'template', 'assets')