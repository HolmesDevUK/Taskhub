from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    title = models.CharField(max_length=255)
    decription = models.TextField()
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={"role": "client"})
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    deadline = models.DateTimeField()
    file = models.FileField(upload_to="task_files/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.client.email}"