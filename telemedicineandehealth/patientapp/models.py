from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from hospitalapp.models import HospitalDoctor
from medicalapp.models import Medicines
# Create your models here.
# for appointing patient
class PatientAppoinmnt(models.Model):
    # hospital_name foreign key
    gender_choice=[('MALE','male'),('FEMALE','female'),('OTHER','other')]
    patient_name=models.CharField(max_length=50)
    patient_gender=models.CharField(max_length=20,choices=gender_choice)
    patient_contact=models.IntegerField()
    patient_email=models.EmailField(unique=True)
    patient_date=models.DateTimeField()
    patient_address=models.CharField(max_length=256)
    def __str__(self):
        return self.patient_name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk': self.id})

class Patient(models.Model):
    gender_choice=[('MALE','male'),('FEMALE','female'),('OTHER','other')]
    patient_hospital=models.CharField(max_length=256)#foreign key with hospitalname
    patient_registration_number=models.IntegerField(unique=True)
    patient_name=models.CharField(max_length=50)
    patient_contact=models.IntegerField()
    patient_gender=models.CharField(max_length=20,choices=gender_choice,default='male',null=True)
    patient_address=models.CharField(max_length=256)
    patient_symptoms=models.TextField()
    patient_age=models.FloatField()
    # patient_email=models.EmailField(unique=True) # present in above class
    # patient_image = models.ImageField(upload_to='patient',null = True)

# prescription given by doctor to patient
class PatientPrescription(models.Model):
    patient_registration_number=models.OneToOneField(Patient,on_delete=models.CASCADE)# one to one filed
    patient_name=models.CharField(max_length=50)
    patient_doctor_name=models.CharField(max_length=50)
    patient_diet=models.TextField()
    patient_medicines=models.ForeignKey(Medicines,on_delete=models.CASCADE)
    patient_progress=models.CharField(max_length=520)

class PatientDiet(models.Model):
    patient_registration_number=models.ForeignKey(Patient,on_delete=models.CASCADE)# regsiterationn is forering key of patient
    do_s=models.TextField()
    don_t=models.TextField()


# for history record of our patient
class PatientAdmit:
    patient_registration_number=models.OneToOneField(Patient,on_delete=models.CASCADE)# one to one filed
    patient_name=models.OneToOneField(Patient,on_delete=models.CASCADE) # one to one field with patient class
    patient_room_number=models.IntegerField()
    patient_bed_number=models.IntegerField()
    patient_doctor_name=models.ForeignKey(HospitalDoctor,on_delete=models.CASCADE)# foreign key with hosital doctor
    patient_admit_date=models.DateTimeField(default=timezone.now())
    patient_discharge_date=models.DateTimeField(null=True)
    # patient_progress=models.TextField()
