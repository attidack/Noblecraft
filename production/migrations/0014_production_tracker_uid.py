# Generated by Django 3.1.2 on 2020-10-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0013_twisting_preroll_1g_manuf'),
    ]

    operations = [
        migrations.AddField(
            model_name='production_tracker',
            name='UID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]