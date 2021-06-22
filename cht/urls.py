
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authentication.urls')),
    path('',include('activity.urls')),
    path('algorithm/',include('report.urls')),

]
