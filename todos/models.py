from django.db import models
import datetime

class TodoModel(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now)
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title 
    
