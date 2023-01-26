from django.urls import path
from django.views.decorators.csrf import csrf_exempt


from . import views

urlpatterns = [
    path('', views.bills, name='bills'),
    path('new_bill', views.new_bill, name='bill-new'),
    path('create', views.create_bill, name='bill-create'),

]

