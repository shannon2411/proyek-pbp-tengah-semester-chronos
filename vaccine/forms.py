from django import forms
from vaccine.models import Vaccine

class VaccineSearchForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['vaccine_name']