from django.shortcuts import render
from django.http import HttpResponseBadRequest,HttpResponse
from django.views.decorators.http import require_http_methods
from .models import CustomUser
from database.models import DailyData, EntryData

import json 

from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from django_expiring_token.models import ExpiringToken
from django_expiring_token.authentication import token_expire_handler

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def user_login(request):
    data = json.loads(request.body)
    username = data["email"]
    password = data["password"]
    if username is None or password is None:
        return Response({'error': 'Please provide both email and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    login(request, user)
    token, _ = ExpiringToken.objects.get_or_create(user=user)
    is_expired, token = token_expire_handler(token)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
@permission_classes((AllowAny,))
def user_signup(request):
    data = json.loads(request.body)
    username = data["email"]
    password = data["password"]
    if username is None or password is None:
        return Response({'error': 'Please provide both email and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = CustomUser.objects.create_user(username,email=username,password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = ExpiringToken.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
    

  

@api_view(['POST'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def user_logout(request):
    #data = json.loads(request.body)
    username = request.user.username
    request.user.auth_token.delete()

    return Response({'message':'the user with ' + username +  ' is logged out'})


        
