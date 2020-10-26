from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Inventory_Log(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    supply = models.CharField(max_length=120)
    supply_amt = models.IntegerField()
    per_box = models.IntegerField(null=True, blank=True)
    Date = models.DateTimeField(auto_now=True)
    UID = models.IntegerField(null=True, blank=True)


    def get_absolute_url(self):
        return reverse('inventory:inventory-detail', kwargs={"id": self.id})
