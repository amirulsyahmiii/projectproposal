# Generated by Django 4.1.7 on 2023-06-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='moisture_data',
            field=models.FloatField(),
        ),
    ]
