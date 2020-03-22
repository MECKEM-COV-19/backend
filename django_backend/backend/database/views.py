from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseBadRequest,HttpResponse
from users.models import CustomUser

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
            patient.zip_code = data['zip']
        if 'flatmates' in data:
            patient.number_of_flatmates = data['flatmates']

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
        dailydata = DailyData.objects.create(patient=patient)
        if 'is_covid_positive' in data:
            dailydata.is_covid_positive = data['isCovidPositive']
        if 'temperature' in data:
            dailydata.temperature = data['temperature']
        if 'has_chills' in data:
            dailydata.has_chills = data['hasChills']
        if 'is_feeling_weak' in data:
            dailydata.is_feeling_weak = data['isFeelingWeak']
        if 'has_body_aches' in data:
            dailydata.has_body_aches = data['hasBodyAches']
        if 'has_continous_cough' in data:
            dailydata.has_continous_cough = data['hasContinousCough']
        if 'has_sniff' in data:
            dailydata.has_sniff = data['hasSniff']
        if 'was_riskzone_last_two_weeks' in data:
            dailydata.was_riskzone_last_two_weeks = data['wasRiskzoneLasTwoWeeks']
        if 'has_diarrhea' in data:
            dailydata.has_diarrhea = data['hasDiarrhea']
        if 'has_continous_cough' in data:
            dailydata.has_continous_cough = data['hasContinousCough']
        if 'has_throat_pain' in data:
            dailydata.has_throat_pain = data['hasThroatPain']
        if 'has_headache' in data:
            dailydata.has_headache = data['hasHeadache']
        if 'is_easier_out_of_breath' in data:
            dailydata.is_easier_out_of_breath = data['isEasierOutOfBreath']
        if 'had_contact_last_two_weeks' in data:
            dailydata.had_contact_last_two_weeks = data['hadContactLastTwoWeeks']
        dailydata.save()
        serialized_daily = serializers.DailyDataSerializer(dailydata)
        return Response(serialized_daily, HTTP_200_OK)

        

        
    if request.method == "GET":
        if 'date' in data:
            date = request.query_params.get("date")
            daily_data = get_object_or_404(DailyData, timestamp=date)
            serialized_daily = serializers.DailyDataSerializer(daily_data)
            return Response(serialized_daily, HTTP_200_OK)
        else:
            return Response({'error':'You need to provide date.'},HTTP_400_BAD_REQUEST)
            




