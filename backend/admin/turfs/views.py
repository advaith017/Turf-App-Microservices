from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Turfs, User
from .serializers import TurfSerializer
from .producer import publish
import random
import json


class TurfViewSet (viewsets.ViewSet):
    def list(self, request):
        turf = Turfs.objects.all()
        serializer = TurfSerializer (turf, many=True)
        return Response(serializer.data)

    def create(self, request): 
        serializer = TurfSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('turf_created',serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        turf = Turfs.objects.get(id=pk)
        serializer = TurfSerializer(turf)
        return Response(serializer.data)
    
    def update (self, request, pk=None):
        turf = Turfs.objects.get(id=pk)
        serializer = TurfSerializer(instance=turf, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('turf_updated',serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):
        turf = Turfs.objects.get(id=pk)
        turf.delete()
        publish('turf_deleted',pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView (APIView):
    def get(self,_):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })