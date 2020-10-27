from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    rate = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.user.username