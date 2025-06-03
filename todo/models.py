from django.db import models

# Create your models here.
class Todo_user(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
class Task(models.Model):
    username=models.ForeignKey("Todo_user", on_delete=models.CASCADE)
    task=models.CharField(max_length=1000)
    created_at=created_at=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=20)
    def __str__(self):
        return self.task