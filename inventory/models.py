from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


class InventorySupplies(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    supply = models.CharField(max_length=120, null=True, blank=True)
    supply_amt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    number_units_in_box = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_of_box = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.supply

    def get_absolute_url(self):
        return reverse('inventories/inventory_supplies.html', kwargs={"id": self.id})


class StorageLocation(models.Model):
    storage_location = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.storage_location


class Inventory_Log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    supply = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True)
    supply_amt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    Date = models.DateTimeField(blank=True, null=True, auto_now=True, editable=True)
    UID = models.IntegerField(null=True, blank=True)
    cost_of_task = models.IntegerField(null=True, blank=True)
    notes = models.CharField(max_length=120, null=True, blank=True)
    storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, null=True, default=1)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        return super(Inventory_Log, self).save()


    def __str__(self):
        return self.supply

    def get_absolute_url(self):
        return reverse('inventory:inventory-detail', kwargs={"id": self.id})

