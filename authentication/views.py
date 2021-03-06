from django.contrib.auth.models import User
from authentication.models import UserProfile
from authentication.serializer import ExtendedUserSerializer, LoginSerializer, TokenSerializer, UserProfileSerializer, UserSerializer
from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.


class LoginView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = (permissions.AllowAny, )
    serializer_class = LoginSerializer
    def get(self,request):
        return Response({"OK":"ok"},status=status.HTTP_200_OK)
    def post(self, request):
        """
        Checks the credentials (taking firebase **idToken** as input)\
        and returns the **REST Token** (Authentication Token),\
        if the credentials are valid.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        userProfile = UserProfile.objects.filter(user=user)
        response = UserProfileSerializer(userProfile[0])
        return Response(response.data, status.HTTP_200_OK)

class UserView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer
    def get(self,request):
        return Response({"OK":"ok"},status=status.HTTP_200_OK)
    def post(self, request):
        """
        Checks the credentials (taking firebase **idToken** as input)\
        and returns the **REST Token** (Authentication Token),\
        if the credentials are valid.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        useruid = serializer.validated_data['useruid']
        userProfile = UserProfile.objects.get(useruid=useruid)
        response = UserProfileSerializer(userProfile)
        return Response(response.data, status.HTTP_200_OK)

class ExtendedUserView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = (permissions.AllowAny, )
    serializer_class = ExtendedUserSerializer
    def get(self,request):
        return Response({"ok":"ok"},status=status.HTTP_200_OK)
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status.HTTP_200_OK)