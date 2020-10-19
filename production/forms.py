from Employees.models import Employee
from django import forms
from .models import Production_tracker, Tasks

class Productionform(forms.ModelForm):
    Employee = forms.ModelChoiceField(queryset=Employee.objects.all().order_by('First_Name'), name='employee')
    Start_time = forms.DateTimeField(name='starttime')
    End_time = forms.DateTimeField(name='endtime')
    Task = forms.ModelChoiceField(queryset=Tasks.objects.all().order_by('task'), name='task')
    Count = forms.IntegerField(name='count')

    class Meta:
        model = Production_tracker
        fields = [
            'Employee',
            'Start_time',
            'End_time',
            'Task',
            'Count',
        ]