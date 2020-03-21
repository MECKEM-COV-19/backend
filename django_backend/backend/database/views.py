from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseBadRequest,HttpResponse
from database.models import Patient

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


@api_view(['POST','GET'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def patient_data(request):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, user=request.user)
        data = request.data 
        if not data['weight'] and not data['height'] and not data['age']:
            return Response({'error':'Please provide at least one field'}, HTTP_400_BAD_REQUEST) 
        if data['age']:
            patient.age = data['age']
        if data['weight']:
            patient.weight = data['weight']
        if data['height']:
            patient.height = data['height']

        patient.save()
        serialized_patient = serializers.PatientSerializer(patient)

        return Response({serialized_patient.data},HTTP_200_OK)
    if request.method == 'GET':
        patient = get_object_or_404(Patient,user=request.user)
        serialized_patient = serializers.PatientSerializer(patient)
        return Response(serialized_patient.data,HTTP_200_OK)


