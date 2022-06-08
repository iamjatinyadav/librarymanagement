from django.db import models
# Create your models here.

class Student(models.Model):
    sno= models.AutoField(primary_key=True)
    seatno = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    shift = models.CharField(max_length=24)
    address = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    timestamp.editable=True


    def __str__(self) -> str:
        return self.name

