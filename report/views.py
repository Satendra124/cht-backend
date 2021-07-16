from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from report.serializer import ActivityIndexSerializer, IndexSerializer, LocationSerializer, ReportDataSerializer, ReportSerializer, SuggestionSerializer
from report.models import ActivityIndexDiscriptions, Index, Location, Suggestions
from rest_framework import generics
from rest_framework.status import HTTP_200_OK
# Create your views here.

class ActivityIndexView(generics.ListCreateAPIView):
    """
    Pass -1 in either of greater then or less then which will not be used
    """
    serializer_class = ActivityIndexSerializer
    authentication_classes = [TokenAuthentication]
    queryset = ActivityIndexDiscriptions.objects.all()
    #permission_classes = [IsAuthenticated]


class SuggestionView(generics.ListCreateAPIView):
    serializer_class = SuggestionSerializer
    authentication_classes = [TokenAuthentication]
    queryset = Suggestions.objects.all()
    #permission_classes = [IsAuthenticated]
    

class IndexView(generics.ListCreateAPIView):
    serializer_class = IndexSerializer
    authentication_classes = [TokenAuthentication]
    queryset = Index.objects.all()
    #permission_classes = [IsAuthenticated]


class LocationView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    authentication_classes = [TokenAuthentication]
    queryset = Location.objects.all()
    #permission_classes = [IsAuthenticated]


class ReportView(generics.GenericAPIView):
    serializer_class = ReportSerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({"ok":"ok"},status=HTTP_200_OK)
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        report  = serializer.save()
        response = ReportDataSerializer(report)
        return Response(response.data, status=status.HTTP_200_OK)


