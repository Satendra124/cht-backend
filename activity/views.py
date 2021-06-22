from rest_framework import status
from activity.serializer import ActivitySerializer, DetailActivitySerializer, SleepEventSerializer, SleepResponseSerializer
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

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
        response = DetailActivitySerializer(activity)
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