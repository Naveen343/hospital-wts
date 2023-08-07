from django.contrib import admin

# Register your models here.

from .models import Department, Doctor

admin.site.register(Department)
admin.site.register(Doctor)

