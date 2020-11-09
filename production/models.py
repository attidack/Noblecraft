from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from inventory.models import InventorySupplies
# Create your models here.


class Tasks(models.Model):
    task = models.CharField(max_length=120)
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Trimming(models.Model):
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Trimming_a")
    finished_product_amount = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    finished_product_b = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Trimming_b")
    finished_product2_amount = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')


class Grinding(models.Model):
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Grinding")
    finished_product_amount = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    input1 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Grinding_input1")
    input1_amt = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    input2 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Grinding_input2")
    input2_amt = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')


class Pre_roll_1g_manuf(models.Model):
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Open_Pre_roll_1g")
    pre_roll_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Open_Pre_roll_1g_input1")
    cone_amt = models.IntegerField(default='1')
    input2 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Open_Pre_roll_1g_input2")
    canna_amount = models.DecimalField(max_digits=10, decimal_places=2, default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Preroll_half_manuf(models.Model):
    finished_product = models.ForeignKey(
        InventorySupplies,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="Open_Pre_roll_halfg",
        related_query_name="Open_Pre_roll_halfg"
    )
    pre_roll_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Open_Pre_roll_halfg_input1")
    cone_amt = models.IntegerField(default='1')
    input2 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Open_Pre_roll_halfg_input2")
    canna_amount = models.DecimalField(max_digits=10, decimal_places=2, default='.50')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Twisting_Preroll_half_manuf(models.Model):
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Pre_roll_halfg")
    pre_roll_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Pre_roll_halfg_input1")
    input1_amt = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Twisting_Preroll_1g_manuf(models.Model):
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Pre_roll_1g")
    pre_roll_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Pre_roll_1g_input1")
    input1_amt = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Unwrapped_Box_manuf(models.Model):
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Unwrapped_box")
    finished_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Unwrapped_box_input1")
    pre_roll_amt = models.IntegerField(default='10')
    input2 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Unwrapped_box_input2")
    box_amt = models.IntegerField(default='1')
    input3 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Unwrapped_box_input3")
    label_amount = models.IntegerField(default='1')
    input4 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Unwrapped_box_input4")
    canna_sticker_amount = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Finished_Box_manuf(models.Model):
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Box")
    finished_box_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Box_input1")
    input1_amt = models.IntegerField(default='1')
    input2 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Box_input2")
    input2_amt = models.IntegerField(default='1')
    input3 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Box_input3")
    input3_amt = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Finished_Tube_2half_grams_manuf(models.Model):
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Tube_2half")
    finished_2half_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Tube_2half_input1")
    input1_amt = models.IntegerField(default='2')
    input2 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Tube_2half_input2")
    input2_amt = models.IntegerField(default='1')
    input3 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Tube_2half_input3")
    input3_amount = models.IntegerField(default='1')

    def __str__(self):
        return "%s" % self.finished_product

    def get_absolute_url(self):
        return reverse("production:production-tracker", kwargs={"id": self.id})


class Finished_Tube_1_gram_manuf(models.Model):
    finished_product = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Tube_1_gram")
    finished_amt = models.IntegerField(default='1')
    input1 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Tube_1_gram_input1")
    input1_amt = models.IntegerField(default='1')
    input2 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Tube_1_gram_input2")
    input2_amt = models.IntegerField(default='1')
    input3 = models.ForeignKey(InventorySupplies, on_delete=models.CASCADE, blank=True, null=True, related_name="Finished_Tube_1_gram_input3")
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
    notes = models.CharField(max_length=120, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("production:production-detail", kwargs={"id": self.id})

