from django.db import models
from django.urls import reverse
from django.conf import settings


class SimpleBill(models.Model):
    bill_title = models.CharField(max_length=50)

class Bill(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return str(self.name)