from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'Yapılacak'),
        ('in-progress', 'Devam Ediyor'),
        ('done', 'Tamamlandı'),
    ]
    title = models.CharField(max_length=200)
    status=models.CharField(max_length=200) # The status of the task (todo, in-progress, done)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title