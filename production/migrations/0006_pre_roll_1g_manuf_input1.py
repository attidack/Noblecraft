# Generated by Django 3.1.2 on 2020-10-20 03:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0005_auto_20201019_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='pre_roll_1g_manuf',
            name='input1',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]