from django.db import models
from django.urls import reverse

# Create your models here.
class Inventory(models.Model):
    supply = models.CharField(max_length=120)
    supply_amt = models.IntegerField()
    per_box = models.IntegerField()

    def get_absolute_url(self):
        return reverse("inventories:inventory-detail", kwargs={"id": self.id})

class Inventory_Log(models.Model):
    Emp = models.ForeignKey('Employees.Employee', on_delete=models.CASCADE)
    supply = models.CharField(max_length=120)
    supply_amt = models.IntegerField()
    Date = models.DateField()

    def get_absolute_url(self):
        return reverse("inventories:inventory-log", kwargs={"id": self.id})
