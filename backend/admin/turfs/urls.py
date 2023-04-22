from django.contrib import admin
from django.urls import path

from .views import TurfViewSet, UserAPIView

urlpatterns = [
    path('turfs', TurfViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })),
    path('turfs/<str:pk>', TurfViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
    })),
    path('user',UserAPIView.as_view())
]