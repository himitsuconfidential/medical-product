from django.contrib import admin
from .models import *

admin.site.register(ClinicManager)
admin.site.register(MedicalProduct)
admin.site.register(Order)
admin.site.register(OrderItem)

