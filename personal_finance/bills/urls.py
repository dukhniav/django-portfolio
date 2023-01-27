from django.urls import path
from django.views.decorators.csrf import csrf_exempt


from . import views

urlpatterns = [
    path('', views.home, name='bills'),
    path('new', views.new_bill, name='bill-new'),

]

