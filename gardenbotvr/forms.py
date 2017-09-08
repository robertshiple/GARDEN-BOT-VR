from django import forms
from .models import ThreeD


class ThreeDForm(forms.ModelForm):
    class Meta:
        model = ThreeD
        fields = ('file', 'thumb', 'uploaded', 'name', 'type')
