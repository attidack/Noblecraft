# Generated by Django 3.1.2 on 2020-10-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0006_pre_roll_1g_manuf_input1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pre_roll_1g_manuf',
            name='date',
        ),
        migrations.AddField(
            model_name='pre_roll_1g_manuf',
            name='input2',
            field=models.CharField(default='cannabis', max_length=120),
        ),
    ]
