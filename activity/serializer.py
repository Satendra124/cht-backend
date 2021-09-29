from activity.util import Mapbox
from activity.models import Activity, SleepEvent, Survey, UsageData
from rest_framework import serializers
from authentication.models import UserProfile

KEY_ID = "id"
KEY_TIME_START = "time_start"
KEY_TIME_END = "time_end"
KEY_COORDINATE_LAT = "latitude"
KEY_COORDINATE_LNG = "longitude"
KEY_APP_USAGE = "app_usage"
KEY_STEPS = "steps"
KEY_NOISE = "amplitude"
KEY_USAGE = "usagedata"
KEY_MOOD = "moods"
class ActivitySerializer(serializers.ModelSerializer):
    useruid = serializers.CharField()
    def save(self, **kwargs):
        data =  self.validated_data
        time_start = data[KEY_TIME_START]
        time_end = data[KEY_TIME_END]
        latitude = data[KEY_COORDINATE_LAT]
        longitude = data[KEY_COORDINATE_LNG]
        amplitude = data[KEY_NOISE]
        moods = data[KEY_MOOD]
        useruid = data['useruid']
        steps = data[KEY_STEPS]
        user = UserProfile.objects.get(useruid=useruid)
        placeName = Mapbox.get_place_from_lat_lng(lat=latitude,lng=longitude)
        activity = Activity.objects.create(latitude=latitude,longitude=longitude,amplitude=amplitude,user=user,steps=steps,time_start=time_start,time_end=time_end,place=placeName,moods=moods)
        return activity

    def validate(self, attrs):
        data =  attrs
        useruid = data['useruid']
        if not validateUser(useruid=useruid): raise serializers.ValidationError({"error":"User Not Found"})
        return attrs
    
    class Meta:
        model = Activity
        fields = ('latitude','longitude','amplitude','useruid','steps','time_start' ,'time_end','moods')

class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageData
        fields = '__all__'

class ActivityResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class SleepEventSerializer(serializers.ModelSerializer):
    useruid = serializers.CharField()
    def save(self, **kwargs):
        data =  self.validated_data
        time_start = data['time_start']
        time_end = data['time_end']
        useruid = data['useruid']
        user = UserProfile.objects.get(useruid=useruid)
        sleepevent = SleepEvent.objects.create(user=user,time_start=time_start,time_end=time_end)
        return sleepevent

    def validate(self, attrs):
        data =  attrs
        useruid = data['useruid']
        if not validateUser(useruid=useruid): raise serializers.ValidationError({"error":"User Not Found"})
        return attrs
    
    class Meta:
        model = SleepEvent
        fields = ('useruid','time_start','time_end')

class SleepResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepEvent
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'

class FetchActivitySerializer(serializers.Serializer):
    useruid = serializers.CharField()
    typeOfData = serializers.IntegerField()
    def validate(self, attrs):
        data =  attrs
        useruid = data['useruid']
        if not validateUser(useruid=useruid): raise serializers.ValidationError({"error":"User Not Found"})
        if data['typeOfData'] != 1 and data['typeOfData'] != 7 and data['typeOfData'] != 30: raise serializers.ValidationError({"error":"Invalid range"})
        return attrs
    def save(self, **kwargs):
        return super().save(**kwargs)



def validateUser(useruid):
    user = UserProfile.objects.filter(useruid=useruid)
    if len(user)==0: return False
    return True
