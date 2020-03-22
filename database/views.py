
from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseBadRequest,HttpResponse
from users.models import CustomUser
import datetime
from .models import DailyData, EntryData

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

from . import serializers


import json

@api_view(['POST','GET'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def patient_data(request):
    if request.method == 'POST':
        patient = request.user
        data = json.loads(request.body)
     
        #print(data)
        if not data['zip'] and not data['flatmates']:
            return Response({'error':'Please provide at least one field'}, HTTP_400_BAD_REQUEST) 
        if 'zip' in data:
            patient.zipCode = data['zip']
        if 'flatmates' in data:
            patient.numberOfFlatmates = data['flatmates']

        patient.save()
        serialized_patient = serializers.PatientSerializer(patient)

        return Response(serialized_patient.data,HTTP_200_OK)
    if request.method == 'GET':
        patient = request.user
        serialized_patient = serializers.PatientSerializer(patient)
        return Response(serialized_patient.data,HTTP_200_OK)


@api_view(['POST','GET'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def daily_data(request):
    if request.method == "POST":
        patient = request.user
        data = json.loads(request.body)
        dailydata , _ = DailyData.objects.create(patient=patient)
        if 'isovidPositive' in data:
            dailydata.isCovidPositive = data['isCovidPositive']
        if 'temperature' in data:
            dailydata.temperature = data['temperature']
        if 'hashills' in data:
            dailydata.hasChills = data['hasChills']
        if 'isFeelingWeak' in data:
            dailydata.isFeelingWeak = data['isFeelingWeak']
        if 'hasBodyAches' in data:
            dailydata.hasBodyAches = data['hasBodyAches']
        if 'cough' in data:
            dailydata.hasContinousCough = data['cough']
        if 'generalFeeling' in data:
            dailydata.generalFeeling = data['generalFeeling']
        if 'hasSniff' in data:
            dailydata.hasSniff = data['hasSniff']
        if 'wasRiskzoneLastTwoWeeks' in data:
            dailydata.wasRiskzoneLastTwoWeeks = data['wasRiskzoneLasTwoWeeks']
        if 'hasDiarrhea' in data:
            dailydata.hasDiarrhea = data['hasDiarrhea']
        if 'hasContinousCough' in data:
            dailydata.hasContinousCough = data['hasContinousCough']
        if 'hasThroatPain' in data:
            dailydata.hasThroatPain = data['hasThroatPain']
        if 'hasHeadache' in data:
            dailydata.hasHeadache = data['hasHeadache']
        if 'isEasierOutOfBreath' in data:
            dailydata.isEasierOutOfBreath = data['isEasierOutOfBreath']
        if 'hadContactLastTwoWeeks' in data:
            dailydata.hadContactLastTwoWeeks = data['hadContactLastTwoWeeks']
        if 'breathingPattern' in data:
            dailydata.breathingPattern = data['breathingPattern']
            
        dailydata.save()
        serialized_daily = serializers.DailyDataSerializer(dailydata)
        return Response(serialized_daily.data, HTTP_200_OK)

        

        
    if request.method == "GET":
        if 'date' in data:
            date = request.query_params.get("date")
            daily_data = get_object_or_404(DailyData, timestamp=date)
            serialized_daily = serializers.DailyDataSerializer(daily_data)
            return Response(serialized_daily.data, HTTP_200_OK)
        else:
            return Response({'error':'You need to provide date.'},HTTP_400_BAD_REQUEST)
            




@api_view(['POST','GET'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def entry_data(request):
    if request.method =="POST":
        patient = request.user
        data = json.loads(request.body)
        entrydata, _ = EntryData.objects.get_or_create(patient=patient)
        if 'hasDisease' in data:
            entrydata.has_disease = data['hasDisease']
        if 'disease' in data:
            entrydata.disease = data['disease']
        if 'height' in data:
            entrydata.height = data['height']
        if 'weight' in data:
            entrydata.weight = data['weight']
        if 'hasMedication' in data:
            entrydata.has_medication = data['hasMedication']
        if 'medication' in data:
            entrydata.medication = data['medication']
        if 'isFluVaccined' in data:
            entrydata.is_flu_vaccined = data['isFluVaccined']
        if 'age' in data:
            entrydata.age = data['age']
        if 'gender' in data:
            entrydata.gender = data['gender']
        entrydata.save()
        serilized_entrydata = serializers.EntryDataSerializer(entrydata)
        return Response(serilized_entrydata.data, HTTP_200_OK)

    if request.method == "GET":
        patient = request.user
        data = json.loads(request.body)
        entrydata = get_object_or_404(EntryData, patient=patient)
        serilized_entrydata = serializers.EntryDataSerializer(entrydata)
        return Response(serilized_entrydata.data, HTTP_200_OK)



@api_view(['GET'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def daily_data_all(request):
    daily = DailyData.objects.filter(patient=request.user)
    if daily:
        serilized = serializers.DailyDataSerializer(daily, many=True)
        return Response(serilized.data, HTTP_200_OK)

    else:
        return Response({'error':'No data yet...'}, HTTP_404_NOT_FOUND)
