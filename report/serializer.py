from report.algorithm import get_report_today_live
from activity.models import DetailActivity
from authentication.models import UserProfile
from django.db.models import fields
from report.models import ActivityIndexDiscriptions, Index, Location, ReportToday, Suggestions
from rest_framework import serializers

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ActivityIndexSerializer(serializers.ModelSerializer):
    index = IndexSerializer(read_only = True)
    class Meta:
        model = ActivityIndexDiscriptions
        fields = '__all__'


class SuggestionSerializer(serializers.ModelSerializer):
    index = IndexSerializer(read_only = True)
    location = LocationSerializer(read_only = True)
    class Meta:
        model = Suggestions
        fields = '__all__'

class ReportTodaySerializer(serializers.Serializer):
    userid = serializers.CharField()
    def save(self, **kwargs):
        data =  self.validated_data
        report = get_report_today_live(userid=data['userid'])
        reportobj,_ = ReportToday.objects.update_or_create(user=UserProfile.objects.get(uid=data['userid']),score = report['score'],indexHours = report['indexHours'])
        for at in report['activityIndexDiscriptions']:
            reportobj.activityIndexDiscriptions.add(at)
        for sg in report['suggestions']:
            reportobj.suggestions.add(sg)
        reportobj.save()
        return reportobj

    def validate(self, attrs):
        data =  attrs
        userid = data['userid']
        if not validateUser(useruid=userid): raise serializers.ValidationError({"error":"User Not Found"})
        return attrs
    

class ReportTodayDataSerializer(serializers.ModelSerializer):
    activityIndexDiscriptions = ActivityIndexSerializer(read_only=True,many=True)
    suggestions = SuggestionSerializer(read_only=True,many=True)
    class Meta:
        model = ReportToday
        fields = ('score','indexHours','activityIndexDiscriptions','suggestions')

def validateUser(useruid):
    user = UserProfile.objects.filter(uid=useruid)
    if len(user)==0: return False
    return True