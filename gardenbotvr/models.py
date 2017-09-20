from django.db import models
import os
from django.utils.text import slugify
import random


class Scene(models.Model):
    """
    scene creator. calls for custom scene html AFRAME file.
    """
    name = models.CharField(max_length=30)
    slug = models.SlugField(editable=False)
    thumb = models.ImageField(upload_to=os.path.join('gardenbotvr', 'scenes'))
    template = models.CharField(max_length=30)
    skycolor = models.CharField(max_length=30, default='#aaffe8')
    groundcolor = models.CharField(max_length=30, default='#c0ff82')
    assets = models.ManyToManyField('Asset')
    radius = models.PositiveIntegerField(default=30)
    ground_material = models.CharField(max_length=30, default='flat')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def render_ground_material(self):
        return f'shader: {self.ground_material}'



class Gltf(models.Model):
    """
    abstract base class for entity and asset. shared fields. no table
    """
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to=os.path.join('gardenbotvr', 'models'))
    thumb = models.ImageField(upload_to=os.path.join('gardenbotvr', 'thumbs'))



    class Meta:
        abstract = True




class Entity(Gltf):
    """
    usable by character. not animated i.e sunflower
    """
    uploaded = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'entities'

    def __str__(self):
        return f'{self.name}'

    def to_aframe_code(self):
        return f'<a-gltf-model src="{self.file.url}">'


class Coordinate(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    randomize = models.BooleanField(default=False)

    def __str__(self):
        return f'random: {self.randomize} {self.x}, {self.y}, {self.z}'

    def to_aframe_attr(self):
        if self.randomize:
            z = random.randint(-30, 1) #TODO: move these values to the scene
        else:
            z = self.z
        result = f'{self.x} {self.y} {z}'
        return result


class Asset(Gltf):
    """
    assets are scene objects, possibly animated. i.e bird
    """

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

            html = f'''
            <a-gltf-model src="{self.file.url}" position="{self.fchord.to_aframe_attr()}">
                   <a-animation attribute="position" from="{self.fchord.to_aframe_attr()}" 
                   to="{self.bchord.to_aframe_attr()}" delay="0" dur="{self.dchord}" easing="linear" 
                   repeat="indefinite" fill="both"></a-animation></a-gltf-model>
            
            '''
            #
            # html = f'<a-gltf-model src="{self.file.url}" material={self.render_material()} position="{self.fchord.to_aframe_attr()}">' \
            #        f'<a-animation attribute="position" from="{self.fchord.to_aframe_attr()}" ' \
            #        f'to="{self.bchord.to_aframe_attr()}" delay="0" dur="{self.dchord}" easing="linear" ' \
            #        f'repeat="indefinite" fill="both"></a-animation></a-gltf-model>'

        else:
            html = f'<a-gltf-model src="{self.file.url}" position="{self.fchord.to_aframe_attr()}"></a-gltf-model>'
        return html

    def __str__(self):
        return self.name




