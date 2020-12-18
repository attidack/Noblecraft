from django import forms
from .models import Inventory_Log, InventorySupplies


class Inventoryform(forms.ModelForm):
    class Meta:
        model = Inventory_Log
        fields = [
            'user_id',
            'supply',
            'supply_amt',
            'UID',
            'notes',
            'storage_location',
        ]


class InventorySuppliesform(forms.ModelForm):
    class Meta:
        model = InventorySupplies
        fields = '__all__'