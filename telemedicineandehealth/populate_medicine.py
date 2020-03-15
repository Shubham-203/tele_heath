import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","telemedicineandehealth.settings")
import django
django.setup()
from medicalapp.models import Medical
from faker import Faker
from random import randint
import random
from passlib.hash import pbkdf2_sha256

faker = Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    choice=['yes','no']
    for i in range(n):
        name=faker.name()
        address=faker.address()
        delivery=random.choice(choice)
        number=phonenumbergen()
        email=faker.email()
        password=faker.password()
        password=pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)

        medical_recor=Medical.objects.get_or_create(medical_name=name,medical_contact=number,medical_address=address,medical_email=email,
        medical_password=password,online_delivery=delivery)
populate(30)
