from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):


    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            null=True,
            blank=True
        )

    PriorityChoices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    StatusChoices = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('On Hold', 'On Hold'),
        ('Not Started', 'Not Started'),
        ('In Review', 'In Review'),
        ('Needs Clarification', 'Needs Clarification'),
        ('Testing in Progress', 'Testing in Progress'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PriorityChoices, default='medium')
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=StatusChoices, default='Not Started')
    file = models.FileField(upload_to='task_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

