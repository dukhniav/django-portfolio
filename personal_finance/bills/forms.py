from django.forms import ModelForm

from .models import Bill

class NewBillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ['name','amount', 'due_date', 'frequency']