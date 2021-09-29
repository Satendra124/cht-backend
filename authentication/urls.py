
from authentication.views import LoginView,UserView,ExtendedUserView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('user/extended/',ExtendedUserView.as_view())
]
