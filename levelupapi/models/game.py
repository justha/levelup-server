"""Game model module"""
from django.db import models


class Game(models.Model):
    """Game database model"""
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="games")
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="games")
    title = models.CharField(max_length=75)
    maker = models.CharField(max_length=75, default='')
    skill_level = models.IntegerField()
    number_of_players = models.IntegerField()