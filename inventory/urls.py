from django.urls import path
from .views import (
    InventoryLog,
    inventorycreateview,
    inventorydetailview,
    inventoryupdateview,
    productiondeleteview,

)
app_name ='inventory'
urlpatterns = [
    path('', InventoryLog.as_view(), name='inventory-log'),
    path('create/', inventorycreateview.as_view(), name='inventory-create'),
    path('<int:id>/', inventorydetailview.as_view(), name='inventory-detail'),
    path('<int:id>/update/', inventoryupdateview.as_view(), name='inventory-update'),
    path('<int:id>/delete/', productiondeleteview.as_view(), name='production-delete'),


]
