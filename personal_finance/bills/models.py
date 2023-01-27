from django.db import models
from django.conf import settings
from datetime import date
from django.contrib.auth.models import User


class BillType(models.Model):
    bill_type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.bill_type)


class Bill(models.Model):
    RECURRING_CHOICES = [
        ('1', 'One time only'),
        ('2', 'Weekly'),
        ('3', 'Every 2 weeks'),
        ('4', 'Monthly'),
        ('5', 'Every 2 months'),
        ('6', 'Quarterly'),
        ('7', 'Every 6 months'),
        ('8', 'Yearly'),
    ]

    REMINDER_CHOICES = [
        ('1', 'None'),
        ('2', '1 day'),
        ('3', '2 days'),
        ('4', '3 days'),
        ('5', '1 week'),
        ('6', '2 weeks'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    due_date = models.DateField(
        auto_now=False, auto_now_add=False, default=date.today)
    bill_type = models.ForeignKey(BillType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    recurring = models.CharField(
        max_length=24, choices=RECURRING_CHOICES, default='1', blank=False, null=False)
    reminder = models.CharField(
        max_length=24, choices=REMINDER_CHOICES, default='1', blank=False, null=False)
    due_date_reminder = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    payment_date = models.DateField(
        auto_now=False, auto_now_add=False, default=date.today)

    class Meta:
        """
        Meta Information
        """
        app_label = "bills"
        db_table = "bills"
        verbose_name = "bill_item"
        verbose_name_plural = "bill_items"

    def __str__(self):
        return str(self.title)
