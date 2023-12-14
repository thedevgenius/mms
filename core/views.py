from django.shortcuts import render
from mess.models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from mess.utils import *
c_m = datetime.now().month
c_y = datetime.now().year
p_m = GetPrevMonth()
p_y = GetPrevYear()


def HomePage(request):
    
    return render(request, 'index.html')

@login_required
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
        #print(diposit)
    try:
        prev_bill = Bill.objects.get(user_id=request.user.id, date__month=p_m, date__year=p_y)
        due = int(prev_bill.due_or_return)
    except:
        due = 0
    



    #print(bazar_count)
    data = {
        'total_mill' : total_mill,
        'diposit' : diposit,
        'bazar_count' : bazar_count,
        'due' : due,
        #'prev_bill' : prev_bill

    }

    return render(request, 'account/dashboard.html', data)