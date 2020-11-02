"""Game model module"""
from django.db import models


class Game(models.Model):
    """Game database model"""
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    skill_level = models.IntegerField() 
    number_of_players = models.IntegerField()