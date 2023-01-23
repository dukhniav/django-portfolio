from django.db import models
from django.conf import settings

class TodoItem(models.Model):
    """
    Todo item model
    """
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todo_item')

    class Meta:
        """
        Meta info
        """
        app_label = 'todo'
        db_table = 'todo_item'
        verbose_name = 'todo_item'
        verbose_name_plural = 'todo_items'

    def __str__(self) -> str:
        return self.name
