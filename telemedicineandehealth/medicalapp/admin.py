from django.contrib import admin
from medicalapp.models import Medical

# Register your models here.
class MedicalAdmin(admin.ModelAdmin):
    list_display=['id','medical_name','medical_address','online_delivery','medical_contact','medical_password']

admin.site.register(Medical,MedicalAdmin)
