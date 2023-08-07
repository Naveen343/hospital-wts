from django.shortcuts import render
from django.db.models import Q
from visitors.models import Appointment

def appointments_list(request):
    search_query = request.GET.get('q', '')
    doctor_group = request.GET.get('doctor_group', '')

    if search_query:
        appointments = Appointment.objects.filter(
            Q(name__icontains=search_query) | Q(mobile_number__icontains=search_query)
        )
    else:
        appointments = Appointment.objects.all()

    if doctor_group:
        appointments = appointments.filter(doctor_id=doctor_group)

    context = {
        'appointments': appointments,
    }
    return render(request, 'hospital/appointments_list.html', context)
