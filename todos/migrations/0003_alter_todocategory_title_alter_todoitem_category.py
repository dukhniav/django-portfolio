# Generated by Django 4.1.5 on 2023-01-23 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todoitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todocategory',
            name='title',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='category',
            field=models.ForeignKey(default='General', on_delete=django.db.models.deletion.CASCADE, to='todos.todocategory', to_field='title'),
        ),
    ]