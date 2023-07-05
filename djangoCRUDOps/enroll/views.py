from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def add_show(request):
    if request.method == "POST": 
        fm = StudentRegistration(request.POST)
        print(fm)

    else: 
        fm = StudentRegistration()

    return render(request, 'enroll/addandshow.html', {'form':fm})