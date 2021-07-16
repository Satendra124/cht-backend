
from authentication.views import LoginView,UserView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('user/',UserView.as_view())
]
