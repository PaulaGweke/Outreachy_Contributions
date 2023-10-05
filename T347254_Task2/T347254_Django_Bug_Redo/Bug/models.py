from django.db import models
import datetime

class Bug(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    BUG_TYPES = [
        ('ERROR', 'Error'),
        ('FEATURE', 'New Feature'),
        ('ENHANCEMENT', 'Enhancement'),
        ('OTHER', 'Other'),
    ]

    bug_type = models.CharField(
        max_length=50,
        choices=BUG_TYPES,
        default='ERROR',  # Default bug type
    )

    report_date = models.DateField(
        default=datetime.date.today
    )

    STATUS_CHOICES = [
        ('TO_DO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='TO_DO',  # Default status when a bug is created
    )

    def __str__(self):
        return self.title  # Display the bug title in admin
