from bson import json_util
from rest_framework import permissions, viewsets, status, views, generics
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core import serializers
from api.models import Result
from api.serializers.UserSerializer import UserSerializer
from rest_framework.renderers import JSONRenderer
from api.serializers.ResultSerializer import ResultSerializer

class ResultList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    # print(queryset)
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ResultSerializer(queryset, many=True)
        return Response(serializer.data)

class ResultInfo(generics.GenericAPIView):
    queryset = Result.objects
    serializer_class = ResultSerializer

    def get(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status = status.HTTP_404_NOT_FOUND)
        data = {}
        if operator:
            data["message"] = "Delete result successful"
        else:
            data["message"] = "Delete result failed"
        return Response(data=data)

    def post(self, request, *args, **kwargs):
        obj = Result()
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        lookup_field = 'pk'
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATE)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
