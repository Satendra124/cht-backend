
from report.views import ActivityIndexView, IndexView, LocationView, ReportTodayView, SuggestionView
from django.urls import path

urlpatterns = [
    path('activityIndex/', ActivityIndexView.as_view()),
    path('suggestions/', SuggestionView.as_view()),
    path('index/', IndexView.as_view()),
    path('location/', LocationView.as_view()),
    path('report/today/', ReportTodayView.as_view()),   
]
