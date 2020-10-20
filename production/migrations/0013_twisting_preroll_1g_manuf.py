# Generated by Django 3.1.2 on 2020-10-20 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0012_auto_20201020_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twisting_Preroll_1g_manuf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished_product', models.CharField(max_length=120)),
                ('pre_roll_amt', models.IntegerField()),
                ('input1_amt', models.IntegerField()),
                ('input1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='production.pre_roll_1g_manuf')),
            ],
        ),
    ]