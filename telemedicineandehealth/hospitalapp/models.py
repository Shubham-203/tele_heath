from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.
class Hospital(models.Model):
    user_choice =(('multi-speciality','multispeciality'),('speciality','speciality'))
    choice = (('yes','yes'),('no','no'))
    hospital_name=models.CharField(max_length=50)
    hospital_address=models.CharField(max_length=50)
    hospital_info=models.TextField()
    hospital_type=models.CharField(max_length=20,choices=user_choice, default='multi-speciality')
    goverment_scheme=models.TextField()
    hospital_contact=models.IntegerField()
    hospital_speciality=models.TextField()
    membership_available=models.CharField(max_length=20,default='no',choices=choice)
    blood_bank=models.CharField(max_length=20,default='yes',choices=choice)
    hospital_lab=models.CharField(max_length=20,default='yes',choices=choice)
    hospital_ambulance=models.CharField(max_length=20,default='yes',choices=choice)
    hospital_bed=models.IntegerField()
    hospital_icu=models.IntegerField()
    hospital_email=models.EmailField(unique=True)
    hospital_password=models.CharField(max_length=50)

    def varify_password(self,raw_password):
        return pbkdf2_sha256.verify(raw_password,self.hospital_password)

class DoctorSpeciality(models.Model):
    degree_choice = (('MBBS','MBBS'),('MD','MD'),('DNB','DNB'),('ENT','ENT'),('MS','MS'),('DCH','DCH'),('BAMS','BAMS'),('BDS','BDS'),
    ('BUMS','BUMS'),('BHMS','BHMS'),('BYNS','BYMS'),('BVSc&AH','BVSc&AH'),('BPT','BPT'))
    speciality_choice=(('Optometry','Optometry'),('DM&MCH','DM&MCH'),('BOT','BOT'),('Cardiology','Cardiology'),('Neurosergery','Neurosergery'),('Pediatrics','Pediatrics'),('Psychiatry','Psychiatry'))
    hospital_name=models.ForeignKey(Hospital,on_delete=models.CASCADE)
    doctor_qualification=models.CharField(max_length=20,choices=degree_choice)
    doctor_speciality=models.CharField(max_length=20,choices=speciality_choice)

class HospitalDoctor(models.Model):
    gender_choice=[('MALE','male'),('FEMALE','female'),('OTHER','other')]
    hospital_name=models.ForeignKey(Hospital,on_delete=models.CASCADE)
    doctor_name=models.CharField(max_length=20)
    doctor_qualification=models.CharField(max_length=20)# chooices)
    doctor_experience=models.FloatField()
    doctor_gender=models.CharField(max_length=20,choices=gender_choice)
    doctor_speciality=models.ManyToManyField(DoctorSpeciality)

class HospitalImages(models.Model):
    hospital_name=models.ForeignKey(Hospital,on_delete=models.CASCADE)
    hospital_image=models.ImageField(upload_to='hospital',null=True)
