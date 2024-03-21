from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=255)
    dep_description = models.TextField()

class Doctors(models.Model):
    doc_name = models.CharField(max_length = 50)
    doc_spec = models.CharField(max_length = 100)
    dep_name = models.ForeignKey(Departments, on_delete = models.CASCADE)

class Booking(models.Model):
    p_name = models.CharField(max_length = 50)
    p_phone = models.CharField(max_length = 10)
    p_email = models.CharField(max_length = 50)
    doc_name = models.ForeignKey(Doctors, on_delete = models.CASCADE)
    booking_date = models.DateField()
    booking_on = models.DateField(auto_now = True)