from django.contrib import admin
from .models import Scene, Entity, Asset, Coordinate, Rotation

admin.site.register(Scene)
admin.site.register(Entity)
admin.site.register(Asset)
admin.site.register(Coordinate)
admin.site.register(Rotation)