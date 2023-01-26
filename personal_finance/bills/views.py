from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.forms import forms
from django.shortcuts import render
from .models import SimpleBill
from .forms import SimpleBillForm

from .models import Bill
from .forms import NewBillForm

def bills(request):
    return render(request, 'bills/home.html')


def new_bill(request):
    """
    Create todo item and view other todo items as well.
    """
    print('test ==========')
    if request.method == 'GET':
        print('----------------------------- IN GET --------------------------')
        context = {'form': NewBillForm()}
        return render(request, 'bills/new_bill.html', context)
    elif request.method == 'POST':
        print('----------------------------- IN POST --------------------------')

        form = NewBillForm(request.POST)
        print('valid?')
        if form.is_valid():
            form.save()
            return redirect('bills')
        else:
            return render(request, 'bills/new_bill.html', {'form': form})




def create_bill(request):
    if request.method == 'GET':
        context = {'form': SimpleBillForm()}
        return render(request, 'bills/create-temp.html', context)
    elif request.method == 'POST':
        form = SimpleBillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'bills/create-temp.html', {'form': form})







def home(request):
    posts = SimpleBill.objects.all()
    context = {'posts': posts}
    return render(request, 'bills/home-temp.html', context)


def about(request):
    return render(request, 'bills/about-temp.html')

      