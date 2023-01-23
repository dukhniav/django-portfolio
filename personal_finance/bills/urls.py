from django.urls import path

from . import views

urlpatterns = [
    path('', views.bills, name='bills'),
    path('new_bill', views.NewBillView.as_view(), name='new_bill') 
]