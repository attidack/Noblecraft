from django.contrib import admin

# Register your models here.
from .models import Tasks, Production_tracker
admin.site.register(Tasks)
admin.site.register(Production_tracker)