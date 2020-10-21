
from django import forms
from .models import Production_tracker, Production_tracker_start, Production_tracker_end

class Productionform(forms.ModelForm):
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

class Productionformstart(forms.ModelForm):
    class Meta:
        model = Production_tracker_start
        fields = [
            'Employee',
            'Start_time',
            'Task',
            'UID'
        ]

class Productionformend(forms.ModelForm):
    class Meta:
        model = Production_tracker_end
        fields = [
            'Employee',
            'End_time',
            'Task',
            'Count',
            'UID'
        ]