import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class Test3D:
    def test_init(self):
        threed = mixer.blend('gardenbotvr.ThreeD')
        assert threed.pk == 1, 'should save an instance'



