import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','telemedicineandehealth.settings')
import django
django.setup()
from doctorapp.models import Doctor
from faker import Faker
import random
from random import randint
from passlib.hash import pbkdf2_sha256
faker=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        gender_choice=['MALE','FEMALE','OTHER']
        degree=['MBBS','MD','DNB','ENT','MS','DCH','BAMS','BDS','BUMS','BHMS','BYMS','BVSc&AH','BPT']
        speciality=['Optometry','DM&MCH','BOT','Cardiology','Neurosergery','Pediatrics','Psychiatry']
        doctor_name=faker.name()
        doctor_qualification=random.choice(degree)
        doctor_experience=randint(1,30)
        doctor_gender=random.choice(gender_choice)
        doctor_speciality=random.choice(speciality)#,choices=list of degrres)
        doctor_contact=phonenumbergen()
        doctor_info=faker.text()
        doctor_email=faker.email()
        doctor_password=faker.password()
        doctor_password=pbkdf2_sha256.encrypt(doctor_password,rounds=12000,salt_size=32)

        doctor_record=Doctor.objects.get_or_create(doctor_name=doctor_name,doctor_qualification=doctor_qualification,doctor_experience=doctor_experience,doctor_gender=doctor_gender,
        doctor_speciality=doctor_speciality,doctor_contact=doctor_contact,doctor_info=doctor_info,doctor_email=doctor_email,doctor_password=doctor_password)
populate(30)
