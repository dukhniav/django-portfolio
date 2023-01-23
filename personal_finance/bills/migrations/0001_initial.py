# Generated by Django 4.1.5 on 2023-01-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_reminders', models.BooleanField()),
                ('is_paid', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('is_recurring', models.BooleanField()),
                ('amount', models.FloatField()),
                ('name', models.TextField(max_length=50)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('next_reminder', models.DateField()),
                ('frequency', models.CharField(choices=[('day', 'Daily'), ('week', 'Weekly'), ('biweek', 'Biweekly'), ('month', 'Monthly'), ('bimonth', 'Bimonthly')], default='month', max_length=9)),
            ],
        ),
    ]