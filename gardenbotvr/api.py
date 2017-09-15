from .serializers import ThreeDSerializer
from rest_framework import viewsets
from .models import ThreeD


class EntityViewSet(viewsets.ModelViewSet):
    queryset = ThreeD.objects.filter(type='ENT')
    serializer_class = ThreeDSerializer


class SceneViewSet(viewsets.ModelViewSet):
    queryset = ThreeD.objects.filter(type='SCN')
    serializer_class = ThreeDSerializer