from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def formfieldarguemts(request):
    fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})
    return render(request, "formfieldarguments/userregistration3.html", {"form":fm})