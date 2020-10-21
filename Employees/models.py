from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    First_Name = models.CharField(max_length=120)
    Last_Name = models.CharField(max_length=120)
    Hire_status = models.CharField(max_length=120)
    Hire_date = models.DateField()
    Rate = models.IntegerField()
    Permit = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    Email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.First_Name, self.Last_Name)

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})