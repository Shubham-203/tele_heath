from hospitalapp.models import Hospital
from django import forms

class HospitalForm(forms.ModelForm):
    class Meta:
        model=Hospital
        fields='__all__'
