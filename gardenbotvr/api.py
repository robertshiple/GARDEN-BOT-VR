from .serializers import ThreeDSerializer
from rest_framework import viewsets
from .models import ThreeD


class ThreeDViewSet(viewsets.ModelViewSet):
    queryset = ThreeD.objects.all()
    serializer_class = ThreeDSerializer