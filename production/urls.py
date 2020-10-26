from django.urls import path
from production.views import (
    ProductionTrackerView,
    ProductionCreateView,
    ProductionDetailView,
    ProductionUpdateView,
    ProductionDeleteView,
    ProductionCreateViewStart,
    ProductionEndView

)
app_name = 'production'
urlpatterns = [
    path('', ProductionTrackerView.as_view(), name='production-tracker'),
    path('create/', ProductionCreateView.as_view(), name='production-create'),
    path('<int:id>/', ProductionDetailView.as_view(), name='production-detail'),
    path('<int:id>/update/', ProductionUpdateView.as_view(), name='production-update'),
    path('<int:id>/delete/', ProductionDeleteView.as_view(), name='production-delete'),
    path('start/', ProductionCreateViewStart.as_view(), name='production-start'),
    path('<int:id>/end/', ProductionEndView.as_view(), name='production-end'),


]
