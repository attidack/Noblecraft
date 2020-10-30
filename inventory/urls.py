from django.urls import path
from .views import (
    InventoryLog,
    inventorycreateview,
    inventorydetailview,
    inventoryupdateview,
    inventorydeleteview,
    InventorySuppliesView,
    InventorySuppliesCreateView,
    InventorySuppliesDetailView,
    InventorySuppliesUpdateView,
    InventorySuppliesDeleteView,


)
app_name ='inventory'
urlpatterns = [
    path('', InventoryLog.as_view(), name='inventory-log'),
    path('create/', inventorycreateview.as_view(), name='inventory-create'),
    path('<int:id>/', inventorydetailview.as_view(), name='inventory-detail'),
    path('<int:id>/update/', inventoryupdateview.as_view(), name='inventory-update'),
    path('<int:id>/delete/', inventorydeleteview.as_view(), name='inventory-delete'),
    path('supplies/', InventorySuppliesView.as_view(), name='inventory-supplies'),
    path('supplies/create/', InventorySuppliesCreateView.as_view(), name='inventory-supplies-create'),
    path('supplies/<int:id>/', InventorySuppliesDetailView.as_view(), name='inventory-supplies-detail'),
    path('supplies/<int:id>/update/', InventorySuppliesUpdateView.as_view(), name='inventory-supplies-update'),
    path('supplies/<int:id>/delete/', InventorySuppliesDeleteView.as_view(), name='inventory-supplies-delete'),


]
