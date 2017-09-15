from django.db import models
import os

# Create your models here.
class ThreeD(models.Model):
    THREE_D_TYPES = (
        ('ENT', 'ENTITY'),
        ('SCN', 'SCENE'),
    )

    file = models.FileField(upload_to=os.path.join('gardenbotvr', 'models'))
    thumb = models.ImageField(upload_to=os.path.join('gardenbotvr', 'thumbs'))
    uploaded = models.DateTimeField()
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=THREE_D_TYPES)

    def __str__(self):
        return f'{self.name} {self.type}'