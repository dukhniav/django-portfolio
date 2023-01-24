from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .models import Bill
from .forms import NewBillForm

def bills(request):
    return render(request, 'bills/home.html')

class NewBillView(CreateView):
    model = Bill
    form_class = NewBillForm
    template_name = 'bills/example.html'
    success_url = 'bills/success.html'