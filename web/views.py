from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def portfolio_home(request):
    return render(request, 'web/home.html')
