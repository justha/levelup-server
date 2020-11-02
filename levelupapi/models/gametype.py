"""Game Type model module"""
from django.db import models


class GameType(models.Model):
    """Game Type database model"""
    desc = models.CharField(max_length=25)

