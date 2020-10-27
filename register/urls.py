from django.urls import path
from .views import register, loginPage

app_name ='register'
urlpatterns = [

    path('', register, name='register'),



]
