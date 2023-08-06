from django.db import models

class Meta:
    app_label = 'visitors'

class Department(models.Model):
    name = models.CharField(max_length=100)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    token_number = models.IntegerField(default=0)
