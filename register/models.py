from django.contrib.auth.models import User
from django.db import models

class HourlyRate(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

