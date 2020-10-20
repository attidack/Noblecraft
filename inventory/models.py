from django.db import models
from django.urls import reverse

# Create your models here.
class Inventory_Log(models.Model):
    Emp = models.ForeignKey('Employees.Employee', on_delete=models.CASCADE)
    supply = models.CharField(max_length=120)
    supply_amt = models.IntegerField()
    per_box = models.IntegerField(null=True, blank=True)
    Date = models.DateTimeField()
    UID = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('inventory:inventory-detail', kwargs={"id": self.id})
