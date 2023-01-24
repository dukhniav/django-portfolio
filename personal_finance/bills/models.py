from django.db import models
from django.urls import reverse

class Bill(models.Model):
    FRQ_CHOICES = (
        ('day','Daily'),
        ('week', 'Weekly'),
        ('biweek','Biweekly'),
        ('month','Monthly'),
        ('bimonth','Bimonthly'),
    )

    # Fields
    enable_reminders = models.BooleanField()
    is_paid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    due_date = models.DateField()
    is_recurring = models.BooleanField()
    amount = models.FloatField()
    name = models.TextField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    next_reminder = models.DateField()
    frequency = models.CharField(max_length=9, choices=FRQ_CHOICES, default='month')



    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("bills_bill_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("bills_bill_update", args=(self.pk,))