import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","telemedicineandehealth.settings")
import django
django.setup()
from patientapp.models import Patient
from faker import Faker
from random import *
# import random

faker = Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        # genders = [ 'female' , 'male' ];
        # gender = faker.randomElements(['male', 'female'])[0]
        # name = faker.name.firstName(gender);
        hname=faker.name()
        registration=faker.random_int(min=10000,max=99999)
        pname=faker.name()
        number=phonenumbergen()
        address=faker.address()
        symptoms=faker.text()
        age=faker.random_int(min=25,max=60)
        patient_recor=Patient.objects.get_or_create(patient_hospital=hname,patient_registration_number=registration,patient_name=pname,patient_contact=number,patient_address=address,patient_symptoms=symptoms,patient_age=age)
populate(30)
