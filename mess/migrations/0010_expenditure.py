# Generated by Django 5.0 on 2023-12-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0009_bill_diposit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('rice', models.IntegerField()),
                ('electric', models.IntegerField()),
                ('cook', models.IntegerField()),
            ],
        ),
    ]
