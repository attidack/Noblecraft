from django import forms
from .models import Production_tracker


class Productionform(forms.ModelForm):
    class Meta:
        model = Production_tracker
        fields = [
            'user_id',
            'Task',
            'Start_time',
            'End_time',
            'Count',
            'UID'
        ]


class ProductionFormStart(forms.ModelForm):
    class Meta:
        model = Production_tracker
        fields = [
            'Task',
            'UID',
        ]


class ProductionFormEnd(forms.ModelForm):
    class Meta:
        model = Production_tracker
        fields = [
            'Count',
        ]
