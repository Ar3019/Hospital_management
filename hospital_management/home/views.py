from django.shortcuts import render
from django.http import HttpResponse

from .models import Departments
from .models import Doctors
from .models import Booking

# Create your views here.
def index(request):
    person = {
        'name': 'June',
        'age': '28',
        'place': 'ekm'
    }
    return render(request, 'index.html', person)

def about(request):
    return render(request, 'about.html')

def booking(request):
    dict_booking = {
        'booking': Booking.object.all()
    }
    return render(request, 'booking.html')

def doctors(request):
    dict_doct = {
        'doct': Doctors.objects.all()
    }
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'department.html', dict_dept)

