# Generated by Django 3.1.2 on 2020-10-20 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0011_auto_20201020_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twisting_preroll_half_manuf',
            old_name='input2_amt',
            new_name='input1_amt',
        ),
    ]
