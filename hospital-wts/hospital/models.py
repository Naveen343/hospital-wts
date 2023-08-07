from django.db import models

class Meta:
    app_label = 'hospital'

class Department(models.Model):
    DEPARTMENT_CHOICES = (
        ('Cardiology', 'Cardiology'),
        ('Orthopedics', 'Orthopedics'),
        ('Gynecology', 'Gynecology'),
        ('Neurology', 'Neurology'),
        # Add more departments as needed
    )

    name = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.get_name_display()

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name+"----"+self.department.name  


