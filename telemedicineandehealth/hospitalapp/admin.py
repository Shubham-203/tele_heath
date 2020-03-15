from django.contrib import admin
from hospitalapp.models import Hospital

# Register your models here.
class HospitalAdmin(admin.ModelAdmin):
    list_display=['id','hospital_name','hospital_address','hospital_type','hospital_contact','hospital_lab','hospital_password']

admin.site.register(Hospital,HospitalAdmin)
