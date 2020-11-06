"""Event model module"""
from django.db import models


class Event(models.Model):
    """Event database model"""
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='events')
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='events')
    day = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=50)
    
