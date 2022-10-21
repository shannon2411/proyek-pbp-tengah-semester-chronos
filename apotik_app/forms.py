from django import forms
from apotik_app.models import Apotik

class ApotikForm(forms.ModelForm):
    class Meta:
        model = Apotik
        fields = ['daerah']