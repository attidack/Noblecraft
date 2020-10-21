from django.urls import path
from register import views as v

app_name ='register'
urlpatterns = [

    path('', v.register, name='register'),


]
