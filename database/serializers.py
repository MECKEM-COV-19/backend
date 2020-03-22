
from rest_framework import serializers

from users import models
from .models import DailyData, EntryData


class PatientSerializer(serializers.ModelSerializer):
    patientId = serializers.UUIDField(format='hex')
    class Meta:
        model = models.CustomUser
        fields = ['email','patientId','zipCode','numberOfFlatmates',]

class DailyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyData
        exclude = ['patient']

class EntryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryData
        exclude = ['patient']
