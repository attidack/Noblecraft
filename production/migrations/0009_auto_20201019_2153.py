# Generated by Django 3.1.2 on 2020-10-20 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0008_auto_20201019_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preroll_half_manuf',
            name='date',
        ),
        migrations.AlterField(
            model_name='preroll_half_manuf',
            name='canna_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]