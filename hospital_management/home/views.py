from django.shortcuts import render
from django.http import HttpResponse

from .models import Departments
from .models import Doctors
from .models import Booking
from .forms import BookingForm

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
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForm()
    dict_form = {
        'form': form
    }
    # dict_booking = {
    #     'booking': Booking.object.all()
    # }
    return render(request, 'booking.html', dict_form)

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

