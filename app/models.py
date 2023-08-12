from django.db import models

# Create your models here.


class TaskModel(models.Model):
    task_title = models.CharField(max_length=30)
    task_description = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title