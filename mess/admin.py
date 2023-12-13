from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Mill)

class DipositAdmin(admin.ModelAdmin):
    list_display = ("date", "user", "amount")

admin.site.register(Diposit, DipositAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display = ("date", "user", "mill", "establish_charge", "mill_cost", "total_cost", "diposit", "due_or_return", "status")

admin.site.register(Bill, BillAdmin)


class EstablishAdmin(admin.ModelAdmin):
    list_display = ("date", "user", "details" ,"amount")

admin.site.register(Establish, EstablishAdmin)


class ExpAdmin(admin.ModelAdmin):
    list_display = ("date", "cook", "electric" ,"rice")

admin.site.register(Expenditure, ExpAdmin)