from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'Incomplete'),
        ('C', 'Complete'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    tags = models.CharField(max_length=200, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

