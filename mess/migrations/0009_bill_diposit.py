# Generated by Django 5.0 on 2023-12-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0008_establish'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='diposit',
            field=models.IntegerField(default=0),
        ),
    ]
