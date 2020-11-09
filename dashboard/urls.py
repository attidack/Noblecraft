from django.urls import path
from dashboard.views import EmployeeDashboard, InventorySummery, StatsView, InventoryDashboard, SupplyList

app_name = 'dashboard'
urlpatterns = [
     path('', EmployeeDashboard.as_view(), name='employee-dashboard'),
     path('inventorysummery/', InventorySummery.as_view(), name='inventory-summery'),
     path('inventorydashboard/', InventoryDashboard.as_view(), name='inventory-dashboard'),
     path('stats/', StatsView.as_view(), name='stats'),
     path('supplylist/<int:supply_id>', SupplyList.as_view(), name='supply-list'),
]
