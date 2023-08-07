from django.shortcuts import render
from django.http import JsonResponse
from hospital.models import Department,Doctor
from .models import Appointment 
from .forms import AppointmentForm

# def create_appointment(request):
    # form = AppointmentForm()
    # if request.method == 'POST':
    #     form = AppointmentForm(request.POST)
    #     if form.is_valid:
            
    #     mobile_number = request.POST.get('mobile_number')
    #     department_id = request.POST.get('department_id')
        
    #     department = Department.objects.get(id=department_id)
    #     doctors = department.doctor_set.all()
    #     total_doctors = doctors.count()
        
    #     appointments_per_doctor = Appointment.objects.filter(department=department).count() // total_doctors
        
    #     # Find the doctor with the least number of appointments
    #     selected_doctor = None
    #     min_appointments = float('inf')
    #     for doctor in doctors:
    #         appointments_count = Appointment.objects.filter(doctor=doctor).count()
    #         if appointments_count < min_appointments:
    #             selected_doctor = doctor
    #             min_appointments = appointments_count
        
    #     token_number = min_appointments // appointments_per_doctor + 1
        
    #     appointment = Appointment.objects.create(
    #         name=name,
    #         mobile_number=mobile_number,
    #         department=department,
    #         doctor=selected_doctor,
    #         token_number=token_number
    #     )
        
    #     return JsonResponse({'token_number': token_number})

def index(request):
    form = AppointmentForm()
    appointment = Appointment.objects.all()
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        
        if form.is_valid:
             p=form.save(commit=False)
             doctors = Doctor.objects.filter(department=p.department)
             print(f'---{doctors}')
             min_count=Appointment.objects.filter(doctor=doctors[0]).count()
             print(f'---{min_count}')
             for doc in doctors:
                 appointments_count = Appointment.objects.filter(doctor=doc).count()
                 
                 if appointments_count <= min_count:
                     p.doctor = doc
                     min_count = appointments_count
             p.save()        
                     
             return render(request,'visitors/success.html')
    context = {'appo': appointment,'form':form}
    return render(request, 'visitors/index.html', context)
