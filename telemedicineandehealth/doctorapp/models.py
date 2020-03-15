from django.db import models
from passlib.hash import pbkdf2_sha256
#Create your models here.
class Doctor(models.Model):
    degree_choice = (('MBBS','MBBS'),('MD','MD'),('DNB','DNB'),('ENT','ENT'),('MS','MS'),('DCH','DCH'),('BAMS','BAMS'),('BDS','BDS'),
    ('BUMS','BUMS'),('BHMS','BHMS'),('BYNS','BYMS'),('BVSc&AH','BVSc&AH'),('BPT','BPT'))
    speciality_choice=(('Optometry','Optometry'),('DM&MCH','DM&MCH'),('BOT','BOT'),('Cardiology','Cardiology'),('Neurosergery','Neurosergery'),('Pediatrics','Pediatrics'),('Psychiatry','Psychiatry'))
    gender_choice=[('MALE','male'),('FEMALE','female'),('OTHER','other')]
    doctor_name=models.CharField(max_length=20)
    doctor_qualification=models.CharField(max_length=20,choices=degree_choice)
    doctor_experience=models.FloatField()
    doctor_gender=models.CharField(max_length=20,choices=gender_choice)
    doctor_speciality=models.CharField(max_length=1000,choices=speciality_choice)
    doctor_contact=models.IntegerField()
    doctor_image=models.ImageField(upload_to='doctor',null=True)
    doctor_info=models.TextField()
    doctor_email=models.EmailField(unique=True)
    doctor_password=models.CharField(max_length=256)

    def varify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.doctor_password)
