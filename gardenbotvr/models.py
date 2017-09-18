from django.db import models
import os


class Scene(models.Model):
    name = models.CharField(max_length=30)
    thumb = models.ImageField(upload_to=os.path.join('gardenbotvr', 'scenes'))
    template = models.CharField(max_length=30)
    skycolor = models.CharField(max_length=30, default='#aaffe8')
    groundcolor = models.CharField(max_length=30, default='#c0ff82')
    assets = models.ManyToManyField('Asset')

    def __str__(self):
        return self.name


class Collada(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to=os.path.join('gardenbotvr', 'models'))
    thumb = models.ImageField(upload_to=os.path.join('gardenbotvr', 'thumbs'))

    class Meta:
        abstract = True


class Entity(Collada):
    uploaded = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'entities'

    def __str__(self):
        return f'{self.name}'


class Coordinate(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    def __str__(self):
        return f'{self.x},{self.y},{self.z}'

    def to_aframe_attr(self):
        result = f'{self.x} {self.y} {self.z}'
        return result


class Asset(Collada):
    is_moving = models.BooleanField(default=False)
    fchord = models.ForeignKey(Coordinate, related_name='from_assets')
    bchord = models.ForeignKey(Coordinate, blank=True, null=True, related_name='to_assets')
    dchord = models.IntegerField(blank=True, null=True)

    def to_aframe_animation(self):
        """
        <a-animation attribute="position" from="-4.585 17.063 29.897" to="-4.585 17.063 -33.181"
        delay="0" dur="36000" easing="linear" repeat="indefinite" fill="both"></a-animation>

        """
        if self.is_moving:
            html = f'<a-collada-model src="{self.file.url}" position="{self.fchord.to_aframe_attr()}">' \
                   f'<a-animation attribute="positon" from="{self.fchord.to_aframe_attr()}" ' \
                   f'to="{self.bchord.to_aframe_attr()}" delay="0" dur="{self.dchord}" easing="linear" ' \
                   f'repeat="indefinite" fill="both"></a-animation><a-collada-model>'

        else:
            html = f'<a-collada-model src="{self.file.url}" position="{self.fchord.to_aframe_attr()}"></a-collada-model>'
        return html

    def __str__(self):
        return self.name




