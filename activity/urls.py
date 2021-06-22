from activity.views import ActivityView, SleepView
from django.urls import path

urlpatterns = [
    path('activity/', ActivityView.as_view()),
    path('sleep/', SleepView.as_view()),
]
