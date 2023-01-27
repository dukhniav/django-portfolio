from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Bill
from .forms import NewBillForm
from django.views import generic
from django.contrib.auth import get_user_model


def home(request):
    bills = Bill.objects.all()
    context = {"bills": bills}

    return render(request, 'bills/home.html', context)


class BillView(generic.DetailView):
    model = Bill
    template_name = 'bills/view_bill.html'


class EditView(generic.DetailView):
    model = Bill
    template_name = 'bills/edit_bill.html'


@login_required
def new_bill(request):
    """
    Create bill and view other bills as well.
    """
    if request.method == 'GET':
        context = {'form': NewBillForm()}
        return render(request, 'bills/new_bill.html', context)
    elif request.method == 'POST':
        form = NewBillForm(request.POST)
        user = get_user_model
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.user_id = request.user.id
            new_bill.save()

            return redirect('bills')
        else:
            return render(request, 'bills/new_bill.html', {'form': form})
