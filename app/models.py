from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(unique=True)

class Comment(models.Model):
    by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reply = models.ManyToManyField('self')

class ToDoModel(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="todos")
    participants = models.ManyToManyField(User, related_name="todo_participants")
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    comments = models.ManyToManyField(Comment, blank=True)
