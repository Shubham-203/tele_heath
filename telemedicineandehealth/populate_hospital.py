import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','telemedicineandehealth.settings')
import django
django.setup()
from hospitalapp.models import Hospital
from faker import Faker
import random
from random import randint
from passlib.hash import pbkdf2_sha256
faker = Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        hospital_choice=['multi-speciality','speciality']
        choice=['yes','no']
        # user_choice =faker.user_choice(('multi-speciality','multispeciality'),('speciality','speciality'))
        # choice=faker.choice(('yes','yes'),('no','no'))
        hospital_name=faker.name()
        hospital_address=faker.address()
        hospital_info=faker.text()
        hospital_type=random.choice(hospital_choice)
        goverment_scheme=faker.text()
        hospital_contact=phonenumbergen()
        hospital_speciality=faker.text()
        membership_available=random.choice(choice)
        blood_bank=random.choice(choice)
        hospital_lab=random.choice(choice)
        hospital_ambulance=random.choice(choice)
        hospital_bed=faker.random_int(min=2,max=40)
        hospital_icu=faker.random_int(min=1,max=10)
        hospital_email=faker.email()
        hospital_password=faker.password()
        hospital_password=pbkdf2_sha256.encrypt(hospital_password,rounds=12000,salt_size=32)

        hospital_record=Hospital.objects.get_or_create(hospital_name=hospital_name,hospital_address=hospital_address,hospital_info=hospital_info,
        hospital_type = hospital_type,goverment_scheme=goverment_scheme,hospital_contact=hospital_contact,hospital_speciality=hospital_speciality,
        membership_available=membership_available,blood_bank=blood_bank,hospital_lab=hospital_lab,hospital_email=hospital_email,
        hospital_password=hospital_password,hospital_ambulance=hospital_ambulance,hospital_bed=hospital_bed,hospital_icu=hospital_icu)
populate(30)
