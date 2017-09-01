from django.db import models
import os

# Create your models here.
class ThreeD(models.Model):
    THREE_D_TYPES = (
        ('PLT', 'Plant'),
        ('FWR', 'Flower'),
        ('OTR', 'Other'),
    )

    file = models.FileField(upload_to=os.path.join('gardenbotvr', 'models'))
    uploaded = models.DateTimeField()
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=THREE_D_TYPES)


    def __str__(self):
        return self.name