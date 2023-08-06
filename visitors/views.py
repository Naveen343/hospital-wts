from django.shortcuts import render
from django.http import JsonResponse
from .models import Department, Appointment

def create_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        department_id = request.POST.get('department_id')
        
        department = Department.objects.get(id=department_id)
        doctors = department.doctor_set.all()
        total_doctors = doctors.count()
        
        appointments_per_doctor = Appointment.objects.filter(department=department).count() // total_doctors
        
        # Find the doctor with the least number of appointments
        selected_doctor = None
        min_appointments = float('inf')
        for doctor in doctors:
            appointments_count = Appointment.objects.filter(doctor=doctor).count()
            if appointments_count < min_appointments:
                selected_doctor = doctor
                min_appointments = appointments_count
        
        token_number = min_appointments // appointments_per_doctor + 1
        
        appointment = Appointment.objects.create(
            name=name,
            mobile_number=mobile_number,
            department=department,
            doctor=selected_doctor,
            token_number=token_number
        )
        
        return JsonResponse({'token_number': token_number})

def index(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'visitors/index.html', context)
