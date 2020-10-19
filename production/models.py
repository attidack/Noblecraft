from django.db import models
from django.urls import reverse

# Create your models here.


class Tasks(models.Model):
    task = models.CharField(max_length=120)
    finished_product = models.CharField(max_length=120)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})

class Pre_roll_1g_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    pre_roll_amt = models.IntegerField()
    cone_amt = models.IntegerField()
    canna_amount = models.IntegerField()

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Preroll_half_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    pre_roll_amt = models.IntegerField()
    cone_amt = models.IntegerField()
    canna_amount = models.IntegerField()

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Box_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    finished_box_amt = models.IntegerField()
    pre_roll_amt = models.IntegerField()
    box_amt = models.IntegerField()
    label_amount = models.IntegerField()
    canna_sticker_amount = models.IntegerField()

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class tube_2half_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    finished_2half_amt = models.IntegerField()
    pre_roll_amt = models.IntegerField()
    plastic_tube = models.IntegerField()
    sticker = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.pre_roll_amt)

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})

class tube_full_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    finished_2half_amt = models.IntegerField()
    pre_roll_amt = models.IntegerField()
    plastic_tube = models.IntegerField()
    sticker = models.IntegerField()

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})

class Production_tracker(models.Model):
    Employee = models.ForeignKey('Employees.Employee', on_delete=models.PROTECT)
    Start_time = models.DateTimeField()
    End_time = models.DateTimeField()
    Task = models.ForeignKey('Tasks', on_delete=models.PROTECT)
    Count = models.IntegerField()

    def get_absolute_url(self):
        return reverse("production:production-detail", kwargs={"id": self.id})
