from typing import Text
from django.db import models
from django.db.models import indexes
from django.db.models.lookups import GreaterThan, LessThan
from authentication.models import UserProfile
# Create your models here.

class Index(models.Model):
    name = models.CharField(max_length=100)
    minHours = models.FloatField()
    maxHours = models.FloatField()
    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    index = models.ForeignKey(Index,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name


class ActivityIndexDiscriptions(models.Model):
    greaterThan = models.FloatField()
    lessThan = models.FloatField()
    text = models.CharField(max_length=200)
    index = models.ForeignKey(Index,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text


class Suggestions(models.Model):
    greaterThan = models.FloatField()
    lessThan = models.FloatField()
    text = models.CharField(max_length=200)
    link = models.URLField()
    index = models.ForeignKey(Index,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.text


class ReportToday(models.Model):
    """
        indexHours - store as 2.3,1.2,0.2 ...
    """
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    score = models.FloatField()
    indexHours = models.TextField()
    activityIndexDiscriptions = models.ManyToManyField(ActivityIndexDiscriptions,blank=True)
    suggestions = models.ManyToManyField(Suggestions,blank=True)
    def __str__(self) -> str:
        return str(self.user) + " " + str(self.score)