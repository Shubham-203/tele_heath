from doctorapp.models import Doctor
from django import forms

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude= ['doctor_image']
        # fields = '__all__'
