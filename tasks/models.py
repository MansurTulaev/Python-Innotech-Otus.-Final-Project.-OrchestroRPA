from django.db import models

class Task(models.Model):
    bot = models.ForeignKey('bots.Bot', on_delete=models.CASCADE)
    command = models.TextField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  # время создания
    updated_at = models.DateTimeField(auto_now=True)      # время обновления
