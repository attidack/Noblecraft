from django.urls import path
from dashboard.views import EmployeeDashboard, OwenDashboard, InventorySummery, StatsView, InventoryDashboard

app_name = 'dashboard'
urlpatterns = [
     path('', EmployeeDashboard.as_view(), name='employee-dashboard'),
     path('owen/', OwenDashboard.as_view(), name='owen-dashboard'),
     path('inventorysummery/', InventorySummery.as_view(), name='inventory-summery'),
     path('inventorydashboard/', InventoryDashboard.as_view(), name='inventory-dashboard'),
     path('stats/', StatsView.as_view(), name='stats'),
]
