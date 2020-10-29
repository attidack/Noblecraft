from django import forms
from .models import Inventory_Log

class Inventoryform(forms.ModelForm):
    class Meta:
        model = Inventory_Log
        fields = [
            'user_id',
            'supply',
            'supply_amt',
            'number_units_in_box',
            'UID'
        ]