from Employees.models import Employee
from production.models import Tasks
from django import forms
from .models import Inventory_Log

class Inventoryform(forms.ModelForm):
    class Meta:
        model = Inventory_Log
        fields = [
            'Emp',
            'supply',
            'supply_amt',
            'per_box',
            'Date',
        ]