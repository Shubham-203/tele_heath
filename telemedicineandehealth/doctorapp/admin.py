from django.contrib import admin
from doctorapp.models import Doctor

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display=['id','doctor_name','doctor_experience','doctor_speciality','doctor_contact','doctor_password']
admin.site.register(Doctor,DoctorAdmin)
