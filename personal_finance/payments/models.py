# payments/models.py
from django.db import models
from django.urls import reverse
from django.conf import settings

class Payment(models.Model):
    bill = models.ForeignKey('bills.Bill', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.bill.title} - {self.amount} - {self.date}'


class PaymentHistory(models.Model):
    bill = models.ForeignKey('bills.Bill', on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.bill.title} - {self.payment.amount} - {self.date} - {self.is_paid}'