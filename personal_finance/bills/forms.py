from django import forms
from django.forms import ModelForm
import datetime
from .models import Bill

class NewBillForm(ModelForm):
    due_date = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Bill
        fields = [
            'title', 
            'due_date', 
            'amount', 
            'recurring',
            'bill_type',
            'reminder',
            'due_date_reminder'
            ]