# Generated by Django 5.0.1 on 2024-01-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_car_transmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
