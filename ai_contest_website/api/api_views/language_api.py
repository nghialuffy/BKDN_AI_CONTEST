from bson import json_util
from rest_framework import permissions, viewsets, status, views
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from api.models.Language import Language
from api.serializers.UserSerializer import UserSerializer
from rest_framework.renderers import JSONRenderer

def index(request):
    list_language = Language.objects.all()
    # serializer_class = UserSerializer

    # if request.method == 'GET':
    #     serializer = UserSerializer(data=list_user)
    #     return JsonResponse(serializer.data, safe=False)
