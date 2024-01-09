from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    STATUSES = (
        ('Active', 'Active'),
        ('Finished', 'Finished'),
        ('Archived', 'Archived')
        
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='note_user')
    status = models.CharField(max_length=255, choices=STATUSES, default='Active')

    def __str__(self):
        return self.title
