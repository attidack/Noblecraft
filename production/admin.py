from django.contrib import admin

# Register your models here.
from .models import(
    Tasks,
    Production_tracker,
    Pre_roll_1g_manuf,
    Preroll_half_manuf,
    Twisting_Preroll_half_manuf,
    Twisting_Preroll_1g_manuf,
    Unwrapped_Box_manuf,
    Finished_Box_manuf,
    Finished_Tube_2half_grams_manuf,
    Finished_Tube_1_gram_manuf
)
admin.site.register(Tasks)
admin.site.register(Production_tracker)
admin.site.register(Pre_roll_1g_manuf)
admin.site.register(Preroll_half_manuf)
admin.site.register(Twisting_Preroll_half_manuf)
admin.site.register(Twisting_Preroll_1g_manuf)
admin.site.register(Unwrapped_Box_manuf)
admin.site.register(Finished_Box_manuf)
admin.site.register(Finished_Tube_2half_grams_manuf)
admin.site.register(Finished_Tube_1_gram_manuf)