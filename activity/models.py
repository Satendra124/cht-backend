from datetime import datetime, timezone
from report.models import Index, Location
from django.db import models
from authentication.models import UserProfile
# Create your models here.


class Activity(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    place = models.CharField(max_length=100)
    amplitude = models.IntegerField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    steps = models.IntegerField()
    moods = models.CharField(max_length=50)
    def __str__(self) -> str:
        return str(self.user)+" " + str(self.time_start)

class Survey(models.Model):
    answer_string = models.CharField(max_length=100)
    useruid = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now())

# class DetailActivity(models.Model):
#     user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     amplitude = models.CharField(max_length=50)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     place = models.ForeignKey(Location,on_delete=models.CASCADE)
#     index = models.ForeignKey(Index,on_delete=models.CASCADE)
#     screenTime = models.IntegerField()
#     is_mocked = models.BooleanField(default=False)
#     steps = models.IntegerField()

#     def __str__(self) -> str:
#         return str(self.user) +" | "+ str(self.place)

class SleepEvent(models.Model):
    time_end = models.DateTimeField()
    time_start = models.DateTimeField()
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.user) + " " + str(self.time_end - self.time_start) 

class UsageData(models.Model):
    useruid = models.CharField(max_length=100)
    usageString = models.TextField()
    date_posted = models.DateField(default=datetime.now)