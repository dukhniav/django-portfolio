from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.forms import forms
from django.shortcuts import render
from .models import Bill
from .forms import NewBillForm

def home(request):
    bills = Bill.objects.all()
    context = {"bills": bills}

    return render(request, 'bills/home.html', context)


def new_bill(request):
    """
    Create todo item and view other todo items as well.
    """
    if request.method == 'GET':
        context = {'form': NewBillForm()}
        return render(request, 'bills/new_bill.html', context)
    elif request.method == 'POST':
        form = NewBillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bills')
        else:
            return render(request, 'bills/new_bill.html', {'form': form})
