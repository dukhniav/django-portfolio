from django.db import models
from django.urls import reverse
from django.conf import settings
from datetime import date


class Bill(models.Model):
    title = models.CharField(max_length=50)
    due_date = models.DateField(auto_now=False, auto_now_add=False,default=date.today)

    def __str__(self):
        return str(self.name)