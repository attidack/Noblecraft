from django.shortcuts import render
from .models import Employee

def Employee(request):
    queryset = Employee.objects.all()
    context ={
        "object_list": queryset
    }
    return render(request, "employees/employee_list.html", context)
