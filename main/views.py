from certifi import contents
from django.shortcuts import render, HttpResponse
from main.models import Student

# Create your views here.
def home(request):
    allstudent = Student.objects.all()
    seatno = Student.objects.raw('SELECT seatno FROM main_Student')
    context = {'allstudent':allstudent,}
    return render(request, 'main/home.html', context)

    

