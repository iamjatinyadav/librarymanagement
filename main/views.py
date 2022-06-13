from certifi import contents
from django.shortcuts import render, HttpResponse
from main.models import Student

# Create your views here.
def home(request):
    list=[]
    list2=[]
    for i in range(1,71):
        list.append(i)
    allstudent = Student.objects.all()
    s=Student.objects.all().values_list('seatno')
    for i in s:
        list2.append(int(i[0]))    
    for y in list2:
        for x in list:
            if y==x:
                list.remove(y)
                break
    
            
    context = {'allstudent':allstudent,'seatavailable':list}
    return render(request, 'main/home.html', context)

    

