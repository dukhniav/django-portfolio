from django.urls import include, path


from . import views

urlpatterns = [
    path('', views.finance_home, name='finance'),
    path('bills/', include('personal_finance.bills.urls')),
]
