from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Student


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    students = Student.objects.all()
    return render(request,'home.html',{'student':students})
def insert(request):
    student = Student()
    student.roll = 'S'
    student.sclass = 'SER'
    student.fname = 'Sibin'
    student.lname = 'Thomas'
    student.save()
    return HttpResponse("Hello, world. You're at the polls index.")
