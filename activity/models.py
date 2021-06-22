from report.models import Index, Location
from django.db import models
from authentication.models import UserProfile
# Create your models here.


class RawActivity(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    soundType = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    screenTime = models.DurationField()
    def __str__(self) -> str:
        return str(self.user)+" " + str(self.timestamp)


class DetailActivity(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    soundType = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Location,on_delete=models.CASCADE)
    index = models.ForeignKey(Index,on_delete=models.CASCADE)
    screenTime = models.DurationField()
    is_mocked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.user) +" | "+ str(self.place)

class SleepEvent(models.Model):
    time_end = models.DateTimeField(auto_now_add=True)
    time_start = models.DateTimeField()
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.user) + " " + str(self.time_end - self.time_start) 