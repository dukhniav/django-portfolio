from django.urls import path

from . import views

urlpatterns = [
    path('', views.bills, name='bills'),
]