from .. import forms
from datetime import datetime


class TestThreeDForm:
    def test_form(self):
        form = forms.ThreeDForm(data={})
        assert form.is_valid() is False, (
            'should be invalid if no data is given'
        )

        data = {'uploaded': datetime, 'name': '', 'type': '',}
        form = forms.ThreeDForm(data=data)
        assert form.is_valid() is False, (
            'should be invalid if body text us less than 10 characters')
        assert 'thumb' in form.errors, 'should return field error for body'

        data = {'file': 'ffonfofn',
                'thumb': 'dondond',
                'uploaded': 'sonsons',
                'name': 'rrobrob',
                'type': 'llamas'}
        form = forms.ThreeDForm(data=data)
        assert form.is_valid() is False, 'should be valid when data is given'
        assert 'type' in form.errors, 'should return field error for body'

