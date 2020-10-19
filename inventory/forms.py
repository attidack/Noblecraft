from Employees.models import Employee
from production.models import Tasks
from django import forms
from .models import Inventory_Log

class Inventoryform(forms.ModelForm):
    supply = forms.CharField(max_length=120)
    supply_amt = forms.IntegerField()
    Date = forms.DateTimeField()

    class Meta:
        model = Inventory_Log
        fields = [
            'Employee',
            'Start_time',
            'End_time',
            'Task',
            'Count',
        ]