from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.
class Medical(models.Model):
    choice = (('yes','yes'),('no','no'))
    medical_name=models.CharField(max_length=20)
    medical_address=models.CharField(max_length=20)
    online_delivery=models.CharField(max_length=20,default='no',choices=choice)
    medical_contact=models.IntegerField()
    medical_email=models.EmailField(unique = True)
    medical_password=models.CharField(max_length=50)
    medicine_file=models.FileField(upload_to='medical/file',null=True)

class Medicines(models.Model):
    medical_name=models.ManyToManyField(Medical)
    medicine_name=models.CharField(max_length=256)

class MedicalImage(models.Model):
    # medical image=foreignkey
    medical_name=models.ForeignKey(Medical,on_delete=models.CASCADE)
    medical_image=models.ImageField(upload_to='medical')
