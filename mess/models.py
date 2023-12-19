from django.db import models
from datetime import datetime
from account.models import *

# Create your models here.
class Mill(models.Model):
    date = models.DateField(unique=True)
    mill = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)

class Diposit(models.Model):
    REASONE_CHOICE = [
        ("B", "Bazar"),
        ("E", "Establishment"),
    ]
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reasone = models.CharField(max_length=1, choices=REASONE_CHOICE, default='B')
    amount = models.IntegerField()

    def __str__(self):
        return str(self.date)
    
class Bill(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mill = models.IntegerField()
    diposit = models.IntegerField(default=0, null=True, blank=True)
    establish_charge = models.FloatField(default=0)
    mill_cost = models.FloatField(default=0)
    total_cost = models.FloatField(default=0)
    due_or_return = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('date', 'user')

    def __str__(self):
        return str(self.date)
    

class Establish(models.Model):
    DETAILS_CHOICE = [
        ("O", "Oil"),
        ("G", "Gas"),
        ("V", "Ginger & Garlic"),
        ("C", "Chili"),
        ("O", "Other"),
    ]

    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.CharField(max_length=1, choices=DETAILS_CHOICE)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.date)
    

class Expenditure(models.Model):
    date = models.DateField(unique=True)
    rice = models.IntegerField()
    electric = models.IntegerField()
    cook = models.IntegerField()


    def __str__(self):
        return str(self.date)