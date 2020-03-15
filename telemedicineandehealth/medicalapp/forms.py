from medicalapp.models import Medical
from django import forms

class MedicalForm(forms.ModelForm):
    class Meta:
        model = Medical
        # fields = '__all__'
        exclude=['medicine_file']
