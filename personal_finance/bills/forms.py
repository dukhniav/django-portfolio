from django import forms
from django.forms import ModelForm
from .models import SimpleBill
from .models import Bill

class NewBillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ['title']



class SimpleBillForm(ModelForm):
    class Meta:
        model = SimpleBill
        fields = ['bill_title']  