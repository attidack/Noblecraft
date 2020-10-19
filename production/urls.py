from django.urls import path
from production.views import (
    production_tracker_view,
    production_create_view,
    production_detail_view,
    production_delete_view,

)
app_name ='production'
urlpatterns = [
    path('', production_tracker_view, name='production-tracker'),
    path('create/', production_create_view, name='production-create'),
    path('<int:id>/', production_detail_view, name='production-detail'),
    path('<int:id>/', production_detail_view, name='production-detail'),
    path('<int:id>/delete/', production_delete_view, name='production-delete'),


]
