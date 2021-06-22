from requests import models
from rest_framework.utils import field_mapping
from activity.util import Mapbox
from activity.models import DetailActivity, RawActivity, SleepEvent
from rest_framework import serializers
from authentication.models import UserProfile
class ActivitySerializer(serializers.ModelSerializer):
    useruid = serializers.CharField()
    def save(self, **kwargs):
        data =  self.validated_data
        latitude = data['latitude']
        longitude = data['longitude']
        soundType = data['soundType']
        useruid = data['useruid']
        screenTime = data['screenTime']
        steps = data['steps']
        user = UserProfile.objects.get(uid=useruid)
        activity = RawActivity.objects.create(latitude=latitude,longitude=longitude,soundType=soundType,user=user,screenTime=screenTime,steps=steps)
        #need place and index
        placeName = Mapbox.get_place_from_lat_lng(lat=latitude,lng=longitude)
        place = Mapbox.get_place(placeName=placeName)
        index = Mapbox.get_index(place=place)
        detailActivity = DetailActivity.objects.create(latitude=latitude,longitude=longitude,soundType=soundType,user=user,place=place,index=index,screenTime=screenTime,steps=steps)
        return detailActivity

    def validate(self, attrs):
        data =  attrs
        useruid = data['useruid']
        if not validateUser(useruid=useruid): raise serializers.ValidationError({"error":"User Not Found"})
        return attrs
    
    class Meta:
        model = RawActivity
        fields = ('latitude','longitude','soundType','useruid','screenTime','steps')

class DetailActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailActivity
        fields = '__all__'


class SleepEventSerializer(serializers.ModelSerializer):
    useruid = serializers.CharField()
    def save(self, **kwargs):
        data =  self.validated_data
        time_start = data['time_start']
        useruid = data['useruid']
        user = UserProfile.objects.get(uid=useruid)
        sleepevent = SleepEvent.objects.create(user=user,time_start=time_start)
        return sleepevent

    def validate(self, attrs):
        data =  attrs
        useruid = data['useruid']
        if not validateUser(useruid=useruid): raise serializers.ValidationError({"error":"User Not Found"})
        return attrs
    
    class Meta:
        model = SleepEvent
        fields = ('useruid','time_start')

class SleepResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepEvent
        fields = '__all__'


def validateUser(useruid):
    user = UserProfile.objects.filter(uid=useruid)
    if len(user)==0: return False
    return True