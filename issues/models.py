from django.db import models

class Issue(models.Model):
    class Priority(models.TextChoices):
        LOW    = 'Low',    'Low'
        MEDIUM = 'Medium', 'Medium'
        HIGH   = 'High',   'High'

    class Status(models.TextChoices):
        OPEN        = 'Open',        'Open'
        IN_PROGRESS = 'In Progress', 'In Progress'
        DONE        = 'Done',        'Done'

    title       = models.CharField(max_length=200)
    description = models.TextField()
    priority    = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    status      = models.CharField(max_length=15, choices=Status.choices,   default=Status.OPEN)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
