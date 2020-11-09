from django.contrib import admin
from .models import InventorySupplies, StorageLocation
# Register your models here.

admin.site.register(InventorySupplies)
admin.site.register(StorageLocation)