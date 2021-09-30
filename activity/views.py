from authentication.models import UserProfile
from activity.models import Activity, Mood, SleepEvent, UsageData
from rest_framework import status
from activity.serializer import ActivityResponseSerializer, ActivitySerializer, DataDumpSerializer, FetchActivitySerializer, MoodSerializer, SleepEventSerializer, SleepResponseSerializer, SurveySerializer, UsageSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime

class DataDump(generics.GenericAPIView):
    serializer_class = DataDumpSerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"ok":"ok"},status=HTTP_200_OK)
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response({"ok":"added"}, status=status.HTTP_200_OK)

class ActivityView(generics.GenericAPIView):
    serializer_class = ActivitySerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"ok":"ok"},status=HTTP_200_OK)
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        activity = serializer.save()
        response = ActivityResponseSerializer(activity)
        return Response(response.data, status=status.HTTP_200_OK)
class UsageView(generics.GenericAPIView):
    serializer_class = UsageSerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"ok":"ok"},status=HTTP_200_OK)
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #serializer.data['usageString'] = usage_serialize(serializer.data['usageString'])
        try:
            q = UsageData.objects.get(useruid=serializer.data['useruid'],date_posted=serializer.data['date_posted'])
            q.usageString = serializer.data['usageString']
            q.save()
        except:
            q = UsageData.objects.create(useruid=serializer.data['useruid'],date_posted=serializer.data['date_posted'],usageString=serializer.data['usageString'])
        response = UsageSerializer(q)
        return Response(response.data, status=status.HTTP_200_OK)


class SleepView(generics.GenericAPIView):
    serializer_class = SleepEventSerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"ok":"ok"},status=HTTP_200_OK)
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        activity = serializer.save()
        response = SleepResponseSerializer(activity)
        return Response(response.data, status=status.HTTP_200_OK)
        
class SurveyView(generics.GenericAPIView):
    serializer_class = SurveySerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"ok":"ok"},status=HTTP_200_OK)
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
class FetchActivity(generics.GenericAPIView):
    serializer_class = FetchActivitySerializer
    authentication_classes = [TokenAuthentication]
    queryset=Activity.objects.all()
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"ok":"ok"},status=HTTP_200_OK)
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        days = serializer.data['typeOfData']
        user = UserProfile.objects.get(useruid=serializer.data['useruid'])
        activities = Activity.objects.filter(user=user,time_start__gte=datetime.datetime.now()-datetime.timedelta(days=days))
        res = ActivityResponseSerializer(activities,many=True)
        usage = UsageData.objects.filter(useruid=serializer.data['useruid'],date_posted__gte=datetime.datetime.now()-datetime.timedelta(days=days))
        usageSerialized = UsageSerializer(usage,many=True)
        sleeps = SleepEvent.objects.filter(user = user,time_start__gte=datetime.datetime.now()-datetime.timedelta(days=days))
        mood =Mood.objects.filter(useruid=serializer.data['useruid'],date_posted__gte=datetime.datetime.now()-datetime.timedelta(days=days))
        moodSeralized = MoodSerializer(mood,many=True)

        result = {
            "activites":res.data,
            "usage":usageSerialized.data,
            "sleep":sleeps,
            "mood":moodSeralized.data
        }
        
        return Response(result, status=status.HTTP_200_OK)

class MoodView(generics.GenericAPIView):
    serializer_class = MoodSerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"ok":"ok"},status=HTTP_200_OK)
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #serializer.data['usageString'] = usage_serialize(serializer.data['usageString'])
        try:
            q = Mood.objects.get(useruid=serializer.data['useruid'],date_posted=serializer.data['date_posted'])
            q.emojiString = serializer.data['emojiString']
            q.save()
        except:
            q = UsageData.objects.create(useruid=serializer.data['useruid'],date_posted=serializer.data['date_posted'],emojiString=serializer.data['emojiString'])
        response = MoodSerializer(q)
        return Response(response.data, status=status.HTTP_200_OK)