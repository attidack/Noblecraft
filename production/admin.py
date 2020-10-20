from django.contrib import admin

# Register your models here.
from .models import Tasks, Production_tracker, Pre_roll_1g_manuf, Finished_Tube_1_gram_manuf
admin.site.register(Tasks)
admin.site.register(Production_tracker)
admin.site.register(Pre_roll_1g_manuf)
admin.site.register(Finished_Tube_1_gram_manuf)