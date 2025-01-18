from django.urls import path
from .views import *

urlpatterns = [
    path('hook/request/', HookAPIView.as_view(), name='index'),
]
