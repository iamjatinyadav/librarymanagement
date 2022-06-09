from certifi import contents
from django.shortcuts import render, HttpResponse
from main.models import Student

# Create your views here.
def home(request):
    allstudent = Student.objects.all()
    context = {'allstudent':allstudent}
    return render(request, 'main/home.html', context)
