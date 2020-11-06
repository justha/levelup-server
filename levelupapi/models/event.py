"""Event model module"""
from django.db import models


class Event(models.Model):
    """Event database model"""
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='events')
    description = models.CharField(max_length=50)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='events')
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)