# Generated by Django 3.2.9 on 2021-11-16 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]