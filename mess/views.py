from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import *
from .models import *
from datetime import datetime
from django.db.models import Sum
from .utils import *
# Create your views here.
current_month = datetime.now().month
current_year = datetime.now().year

previous_month = GetPrevMonth()
previous_year = GetPrevYear()


def Mills(request):
    users = User.objects.filter(is_active=True)
    mills = Mill.objects.filter(date__month=current_month, date__year=current_year)

    data = {
        'users' : users,
        'mills' : mills
    }
    return render(request, 'mess/mills.html', data)

@login_required
def AddMill(request):
    users = User.objects.filter(is_active=True)
    mills = Mill.objects.all()

    if request.method == 'POST':
        date = request.POST['date']
        mill_dict = {}
        total_mill = 0
        for user in users:
            key = f"m-{user.id}"
            mill = request.POST[key]
            mill_dict[str(user.id)] = int(mill)
            total_mill += int(mill)
            bill_user = User.objects.get(id=user.id)

            try:
                bill = Bill.objects.get(user_id=user.id, date__month=previous_month, date__year=previous_year)
                new_mill = bill.mill+int(mill)
                bill.mill = new_mill
                bill.save()
            except:
                #print('not founad')
                Bill.objects.create(
                    date=date,
                    user=bill_user,
                    mill=mill
                )

        user = User.objects.get(id=request.user.id)
        amount = (total_mill*10) + 20

        Mill.objects.create(
            date=date,
            mill=mill_dict,
            user=user,
            amount=amount
        )
        Diposit.objects.create(
            date=date,
            user=user,
            amount=amount
        )

        return redirect('dashboard')
    data = {
        'users' : users,
        'mills' : mills
    }
    return render(request, 'mess/add-mill.html', data)

@login_required
def AddEstablish(request):
    if request.method == 'POST':
        date = request.POST['date']
        user = User.objects.get(id=request.user.id)
        details = request.POST['details']
        amount = request.POST['amount']
        Establish.objects.create(
            date=date,
            user=user,
            details=details,
            amount=amount
        )
        Diposit.objects.create(
            date=date,
            user=user,
            amount=amount
        )
        return redirect('dashboard')

    return render(request, 'mess/add-establish.html')


def Calculate(request):
    exp = Expenditure.objects.get(date__month=previous_month, date__year=previous_year)
    if exp is not None:
        total_mill = Bill.objects.filter(date__month=previous_month, date__year=previous_year).aggregate(Sum('mill'))['mill__sum']
        total_bazar = Mill.objects.filter(date__month=previous_month, date__year=previous_year).aggregate(Sum('amount'))['amount__sum']    
        rice = exp.rice
        
        total_exp = total_bazar+rice
        mill_charge = total_exp/total_mill
        users = User.objects.filter(is_active=True)
        total_user = users.count()

        establish = Establish.objects.filter(date__month=previous_month, date__year=previous_year).aggregate(Sum('amount'))['amount__sum']
        electric_cook = exp.electric + exp.cook
        total_establish = establish + electric_cook
        est_charge = round((total_establish / total_user))


        for user in users:
            diposit = Diposit.objects.filter(user_id=user.id, date__month=previous_month, date__year=previous_year).aggregate(Sum('amount'))['amount__sum']
            if diposit is None:
                diposit = 0
            bill = Bill.objects.get(user_id=user.id, date__month=previous_month, date__year=previous_year)
            bill.establish_charge = est_charge
            mill = bill.mill
            bill.mill_cost = round((mill_charge*mill))
            total_cost = (mill_charge*mill) + est_charge
            bill.total_cost = round(total_cost)
            bill.diposit = diposit
            bill.due_or_return = round((total_cost - diposit))
            if bill.due_or_return <= 0:
                bill.status = True
            bill.save()
    return render(request, 'mess/calculate.html')

def Bills(request):
    bill = Bill.objects.get(user_id=request.user.id, date__month=previous_month, date__year=previous_year)

    data = {
        'bill' : bill
    }

    return render(request, 'mess/bill.html', data)