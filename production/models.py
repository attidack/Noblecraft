from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Tasks(models.Model):
    task = models.CharField(max_length=120)
    finished_product = models.CharField(max_length=120)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Trimming(models.Model):
    finished_product = models.CharField(max_length=120, default='A_bud')
    finished_product_amount = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    finished_product_b = models.CharField(max_length=120, default='B_bud')
    finished_product2_amount = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')


class Grinding(models.Model):
    finished_product = models.CharField(max_length=120, default='A_bud')
    finished_product_amount = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    input1 = models.CharField(max_length=120, default='A_bud')
    input1_amt = models.IntegerField(default='1')
    input2 = models.CharField(max_length=120, default='B_bud')
    input2_amt = models.IntegerField(default='1')


class Pre_roll_1g_manuf(models.Model):
    finished_product = models.CharField(max_length=120, default='1g_open_pre_roll')
    pre_roll_amt = models.IntegerField(default='1')
    input1 = models.CharField(max_length=120, default='cone')
    cone_amt = models.IntegerField(default='1')
    input2 = models.CharField(max_length=120, default='cannabis grams')
    canna_amount = models.DecimalField(max_digits=10, decimal_places=2, default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Preroll_half_manuf(models.Model):
    finished_product = models.CharField(max_length=120, default='halfg_open_pre_roll')
    pre_roll_amt = models.IntegerField(default='1')
    input1 = models.CharField(max_length=120, default='cone')
    cone_amt = models.IntegerField(default='1')
    input2 = models.CharField(max_length=120, default='cannabis grams')
    canna_amount = models.DecimalField(max_digits=10, decimal_places=2, default='.50')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Twisting_Preroll_half_manuf(models.Model):
    finished_product = models.CharField(max_length=120, default='halfg_pre_roll')
    pre_roll_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(Preroll_half_manuf(finished_product), on_delete=models.PROTECT)
    input1_amt = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Twisting_Preroll_1g_manuf(models.Model):
    finished_product = models.CharField(max_length=120, default='1g_pre_roll')
    pre_roll_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(Pre_roll_1g_manuf(finished_product), on_delete=models.PROTECT)
    input1_amt = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Unwrapped_Box_manuf(models.Model):
    finished_product = models.CharField(max_length=120, default='Unwrapped_box')
    finished_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(Twisting_Preroll_half_manuf(finished_product), on_delete=models.PROTECT)
    pre_roll_amt = models.IntegerField(default='10')
    input2 = models.CharField(max_length=120, default='Box')
    box_amt = models.IntegerField(default='1')
    input3 = models.CharField(max_length=120, default='Box_Label')
    label_amount = models.IntegerField(default='1')
    input4 = models.CharField(max_length=120, default='cannasticker')
    canna_sticker_amount = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Finished_Box_manuf(models.Model):
    finished_product = models.CharField(max_length=120, default='Finished_Box')
    finished_box_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(Unwrapped_Box_manuf(finished_product), on_delete=models.PROTECT)
    input1_amt = models.IntegerField(default='1')
    input2 = models.CharField(max_length=120, default='Plastic_wrap')
    input2_amt = models.IntegerField(default='1')
    input3 = models.CharField(max_length=120, default='Ribbon')
    input3_amt = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Finished_Tube_2half_grams_manuf(models.Model):
    finished_product = models.CharField(max_length=120, default='Preroll_tube_2_half_grams')
    finished_2half_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(Twisting_Preroll_half_manuf(finished_product), on_delete=models.PROTECT)
    input1_amt = models.IntegerField(default='2')
    input2 = models.CharField(max_length=120, default='Tube')
    input2_amt = models.IntegerField(default='1')
    input3 = models.CharField(max_length=120, default='Tube_Sticker')
    input3_amount = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Finished_Tube_1_gram_manuf(models.Model):
    finished_product = models.CharField(max_length=120, default='Preroll_tube_1_gram')
    finished_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(Twisting_Preroll_1g_manuf(finished_product), on_delete=models.PROTECT)
    input1_amt = models.IntegerField(default='1')
    input2 = models.CharField(max_length=120, default='Tube')
    input2_amt = models.IntegerField(default='1')
    input3 = models.CharField(max_length=120, default='Tube_Sticker')
    input3_amount = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Production_tracker(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="production", null=True)
    Start_time = models.DateTimeField(blank=True, null=True)
    End_time = models.DateTimeField(blank=True, null=True)
    Task = models.ForeignKey('Tasks', on_delete=models.PROTECT)
    Count = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Count2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    UID = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("production:production-detail", kwargs={"id": self.id})

