from django.test import RequestFactory
import pytest
from .. import views

pytestmark = pytest.mark.django_db

class TestHomeView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = views.home(req)
        assert resp.status_code == 200, 'should be callable by anyone'

class Testcreate_colladaView:
    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = views.home(req)
        assert resp.status_code == 200, 'should be callable by anyone'
