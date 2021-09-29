from activity.views import ActivityView, FetchActivity, SleepView, SurveyView, UsageView
from django.urls import path

urlpatterns = [
    path('activity/', ActivityView.as_view()),
    path('survey/', SurveyView.as_view()),
    path('sleep/',SleepView.as_view()),
    path('activity/query/',FetchActivity.as_view()),
    path('usage/',UsageView.as_view())
]
