"""GardenBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from gardenbotvr.views import home
from django.conf import settings
from django.conf.urls.static import static
from gardenbotvr.views import create_collada, scene
from gardenbotvr.api import EntityViewSet, AssetViewSet, SceneViewSet, CoordinateViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'entity', EntityViewSet)
router.register(r'scene', SceneViewSet)
router.register(r'asset', AssetViewSet)
router.register(r'coordinate', CoordinateViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^threed/create/', create_collada, name='collada'),
    url(r'^api/v1/', include(router.urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^scene/', scene, name='scene'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
