from django.contrib import admin
from .models import User,Patient,Practitioner


admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Practitioner)

# Register your models here.
