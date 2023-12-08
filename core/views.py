from django.shortcuts import render
from mess.models import *
from datetime import datetime
from django.db.models import Sum
c_m = datetime.now().month
c_y = datetime.now().year



def HomePage(request):
    
    return render(request, 'index.html')


def Dashboard(request):
    try:
        bill = Bill.objects.get(user_id=request.user.id, date__month=c_m, date__year=c_y)
        total_mill = bill.mill
    except:
        total_mill = 0

    mills = Mill.objects.filter(user_id=request.user.id, date__month=c_m, date__year=c_y)
    bazar_count = mills.count()
    
    diposit = 0
    diposit = Diposit.objects.filter(user_id=request.user.id, date__month=c_m, date__year=c_y).aggregate(Sum('amount'))['amount__sum']
    if diposit is None:
        diposit = 0
        print(diposit)
    

    #print(bazar_count)
    data = {
        'total_mill' : total_mill,
        'diposit' : diposit,
        'bazar_count' : bazar_count
    }

    return render(request, 'account/dashboard.html', data)