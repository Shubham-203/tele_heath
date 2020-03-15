from patientapp.models import Patient,PatientAppoinmnt
from django import forms

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientAppoinmntForm(forms.ModelForm):
    class Meta:
        model = PatientAppoinmnt
        fields = '__all__'
