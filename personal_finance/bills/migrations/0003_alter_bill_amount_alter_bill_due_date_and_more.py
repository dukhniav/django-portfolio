# Generated by Django 4.1.5 on 2023-01-26 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_remove_bill_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='enable_reminders',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bill',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bill',
            name='is_recurring',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bill',
            name='next_reminder',
            field=models.DateField(null=True),
        ),
    ]