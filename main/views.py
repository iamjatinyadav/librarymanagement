from certifi import contents
from django.shortcuts import render, HttpResponse
from main.models import Student

# Create your views here.
def home(request):
    list=[]
    list2=[]
    for i in range(1,71):
        list.append(i)
    print(list)
    allstudent = Student.objects.all()
    s=Student.objects.all().values_list('seatno')
    for i in s:
        list2.append(int(i[0]))
    print(list2)    
    for y in list2:
        for x in list:
            if y==x:
                list.remove(y)
                break
    print(list)
            
    context = {'allstudent':allstudent,'i':i}
    return render(request, 'main/home.html', context)

    

