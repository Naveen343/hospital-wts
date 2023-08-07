from django.db import models
from hospital.models import Department,Doctor
class Meta:
    app_label = 'visitors'


    
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    token_number = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only update token_number if the record is being created (not updated)
            last_appointment = Appointment.objects.filter(department=self.department).order_by('-token_number').first()
            if last_appointment:
                self.token_number = last_appointment.token_number + 1
            else:
                self.token_number = 1
        super(Appointment, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"Appointment for {self.name} - Token: {self.token_number}"
