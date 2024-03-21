from django.contrib import admin

from .models import Departments
from .models import Doctors
from .models import Booking
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Booking)