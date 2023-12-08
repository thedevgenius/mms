from django.shortcuts import render, redirect
from account.models import *
from .models import *
from datetime import datetime
# Create your views here.
current_month = datetime.now().month
current_year = datetime.now().year

def Mills(request):
    users = User.objects.filter(is_active=True)
    mills = Mill.objects.filter(date__month=current_month, date__year=current_year)

    data = {
        'users' : users,
        'mills' : mills
    }
    return render(request, 'mess/mills.html', data)

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
                bill = Bill.objects.get(user_id=user.id, date__month=current_month, date__year=current_year)
                new_mill = bill.mill+int(mill)
                bill.mill = new_mill
                bill.save()
            except:
                print('not founad')
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