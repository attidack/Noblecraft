from django.contrib import admin

# Register your models here.
from .models import Tasks, Production_tracker, Pre_roll_1g_manuf
admin.site.register(Tasks)
admin.site.register(Production_tracker)
admin.site.register(Pre_roll_1g_manuf)