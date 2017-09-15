from django import forms
from .models import Entity, Scene, Asset


class EntityForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ('file', 'thumb', 'uploaded', 'name')


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('file', 'thumb', 'uploaded', 'name', 'is_moving', 'fchord', 'bchord', 'dchord')


class SceneForm(forms.ModelForm):
    class Meta:
        model = Scene
        fields = ('name', 'groundcolor', 'skycolor', 'template', 'assets')
