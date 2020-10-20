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
    input1 = models.CharField(max_length=120)
    cone_amt = models.IntegerField()
    input2 = models.CharField(max_length=120, default='cannabis')
    canna_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Preroll_half_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    pre_roll_amt = models.IntegerField()
    input1 = models.CharField(max_length=120, default='cone')
    cone_amt = models.IntegerField()
    input2 = models.CharField(max_length=120, default='cannabis')
    canna_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Twisting_Preroll_half_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    pre_roll_amt = models.IntegerField()
    input1 = models.ForeignKey('Preroll_half_manuf', on_delete=models.PROTECT)
    input1_amt = models.IntegerField()

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Twisting_Preroll_1g_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    pre_roll_amt = models.IntegerField()
    input1 = models.ForeignKey('Pre_roll_1g_manuf', on_delete=models.PROTECT)
    input1_amt = models.IntegerField()

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Unwrapped_Box_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    finished_box_amt = models.IntegerField()
    input1 = models.ForeignKey('Twisting_Preroll_half_manuf', on_delete=models.PROTECT)
    pre_roll_amt = models.IntegerField()
    input2 = models.CharField(max_length=120, default='Box')
    box_amt = models.IntegerField()
    input3 = models.CharField(max_length=120, default='Label')
    label_amount = models.IntegerField()
    input4 = models.CharField(max_length=120, default='cannasticker')
    canna_sticker_amount = models.IntegerField()

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Finished_Box_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    finished_box_amt = models.IntegerField()
    input1 = models.ForeignKey('Unwrapped_Box_manuf', on_delete=models.PROTECT)
    input1_amt = models.IntegerField()
    input2 = models.CharField(max_length=120, default='Plastic_wrap')
    input2_amt = models.IntegerField()
    input3 = models.CharField(max_length=120, default='Ribbon')
    input3_amount = models.IntegerField()

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Finished_Tube_2half_grams_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    finished_2half_amt = models.IntegerField()
    input1 = models.ForeignKey('Twisting_Preroll_half_manuf', on_delete=models.PROTECT)
    input1_amt = models.IntegerField()
    input2 = models.CharField(max_length=120, default='Tube')
    input2_amt = models.IntegerField()
    input3 = models.CharField(max_length=120, default='Sticker')
    input3_amount = models.IntegerField()

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})

class Finished_Tube_1_gram_manuf(models.Model):
    finished_product = models.CharField(max_length=120)
    finished_amt = models.IntegerField()
    input1 = models.ForeignKey('Pre_roll_1g_manuf', on_delete=models.PROTECT)
    input1_amt = models.IntegerField()
    input2 = models.CharField(max_length=120, default='Tube')
    input2_amt = models.IntegerField()
    input3 = models.CharField(max_length=120, default='Sticker')
    input3_amount = models.IntegerField()

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})

class Production_tracker(models.Model):
    Employee = models.ForeignKey('Employees.Employee', on_delete=models.PROTECT)
    Start_time = models.DateTimeField()
    End_time = models.DateTimeField()
    Task = models.ForeignKey('Tasks', on_delete=models.PROTECT)
    Count = models.IntegerField()
    UID = models.IntegerField()

    def get_absolute_url(self):
        return reverse("production:production-detail", kwargs={"id": self.id})
