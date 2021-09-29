from authentication.models import UserProfile
from activity.models import Activity, SleepEvent, UsageData
from rest_framework import status
from activity.serializer import ActivityResponseSerializer, ActivitySerializer, FetchActivitySerializer, SleepEventSerializer, SleepResponseSerializer, SurveySerializer, UsageSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime
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
        try:
            q = UsageData.objects.get(useruid=serializer.data['useruid'],date_posted=serializer.data['date_posted'])
            q.usageString = serializer.data['usageString']
            q.save()
        except:
            q= UsageData.objects.create(useruid=serializer.data['useruid'],date_posted=serializer.data['date_posted'],usageString=serializer.data['usageString'])
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
        # result = {
        #     "steps":[],
        #     "sleep":[],
        #     "moods":[],
        #     "amplitudes":[],
        #     "usage":{},
        #     "places":{}
        # }
        user = UserProfile.objects.get(useruid=serializer.data['useruid'])
        activities = Activity.objects.filter(user=user,time_start__gte=datetime.datetime.now()-datetime.timedelta(days=days))
        res = ActivityResponseSerializer(activities,many=True)
        usage = UsageData.objects.filter(useruid=serializer.data['useruid'],date_posted__gte=datetime.datetime.now()-datetime.timedelta(days=days))
        usageSerialized = UsageSerializer(usage,many=True)
        sleeps = SleepEvent.objects.filter(user = user,time_start__gte=datetime.datetime.now()-datetime.timedelta(days=days))
        result = {
            "activites":res.data,
            "usage":usageSerialized.data,
            "sleep":sleeps
        }
        
        return Response(result, status=status.HTTP_200_OK)