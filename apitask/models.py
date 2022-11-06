from django.db import models

# Create your models here.


class Task (models.Model):
  
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return (self.title)

     