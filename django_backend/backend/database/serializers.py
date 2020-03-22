
from rest_framework import serializers

from users import models
from .models import DailyData, EntryData


class PatientSerializer(serializers.ModelSerializer):
    patient_id = serializers.UUIDField(format='hex')
    class Meta:
        model = models.CustomUser
        fields = ['email','patient_id','zip_code','number_of_flatmates',]

class DailyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyData
        exlude = ['patient']

class EntryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryData
        exclude = ['patient']
