from django.db import models

class Point(models.Model):
    name = models.CharField(max_length=100)
    audioUrl = models.TextField(max_length=1000)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    #создать фото к локациям
