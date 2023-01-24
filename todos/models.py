from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.forms import ModelChoiceField


class TodoCategory(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return str(self.title)

class TodoTag(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self) -> str:
        return str(self.title)


class TodoItem(models.Model):
    """
    Todo Item Model
    """    

    PRIORITY_CHOICES = (
        ('1','Low'),
        ('2', 'Normal'),
        ('3','High'),
    )

    title = models.CharField(max_length=100)
    notes = models.TextField(max_length=500, default='')
    category = models.ForeignKey(TodoCategory,on_delete=models.CASCADE)
    priority = models.CharField(max_length=9, choices=PRIORITY_CHOICES, default='1')
    tags = TaggableManager()

    # TODO reorder functionality
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="todo_item")

    is_completed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    
    has_due_date = models.BooleanField(default=False)

    due_date = models.DateTimeField(null=True, default=None)

    has_reminder = models.BooleanField(default=False)
    reminder_date = models.DateTimeField(null=True, default=None)

    has_sub_todos = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        """
        Meta Information
        """
        app_label = "todos"
        db_table = "todos_item"
        verbose_name = "todo_item"
        verbose_name_plural = "todo_items"

    def __str__(self):
        return str(self.name)