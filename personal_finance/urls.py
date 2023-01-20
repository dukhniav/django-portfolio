from django.urls import include, path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bills/', include('personal_finance.bills.urls')),
]