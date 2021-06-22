
from authentication.views import LoginView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view()),
]
