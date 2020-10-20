from Employees.models import Employee
from django import forms
from .models import Production_tracker, Tasks

class Productionform(forms.ModelForm):
    Employee = forms.ModelChoiceField(queryset=Employee.objects.all().order_by('First_Name'))
    Start_time = forms.DateTimeField()
    End_time = forms.DateTimeField()
    Task = forms.ModelChoiceField(queryset=Tasks.objects.all().order_by('task'))
    Count = forms.IntegerField()

    class Meta:
        model = Production_tracker
        fields = [
            'Employee',
            'Start_time',
            'End_time',
            'Task',
            'Count',
            'UID'
        ]