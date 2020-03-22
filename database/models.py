
from django.db import models
from users.models import CustomUser
import uuid

import datetime




class EntryData(models.Model):
    patient = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="entry_data")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    hasDisease = models.BooleanField(null=True)
    disease = models.TextField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    hasMedication = models.BooleanField(null=True)
    medication = models.TextField(null=True)
    isFluVaccined = models.BooleanField(null=True) # Im Zeitraum von Okt19 bis heute
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=(("male","male"),("female","female"),("divers","divers")),max_length=20)


class DailyData(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="daily_data")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    isCovidPositive = models.BooleanField(null=True)
    temperature = models.FloatField(null=True)
    breathingPattern = models.CharField(choices=(('normal','normal'),('biots','biots'),('kussmaul','kussmaul'),('cheynestokes','cheynestokes'),('idontknow','idontknow')),max_length=20)
    hasChills = models.BooleanField(null=True)
    isFeelingWeak = models.BooleanField(null=True)
    hasBodyAches = models.BooleanField(null=True)
    generalFeeling = models.CharField(choices=(('critical','critical'),('bad','bad'),('normal','normal'),('good','good')),max_length=20,null=True)
    cough = models.CharField(choices=(('dry','dry'),('produtive','productive'),('none','none')),max_length=20,null=True)
    hasSniff = models.BooleanField(null=True)
    hasDiarrhea = models.BooleanField(null=True)
    hasThroatPain = models.BooleanField(null=True)
    hasHeadache = models.BooleanField(null=True)
    isEasierOutOfBreath = models.BooleanField(null=True)
    wasRiskzoneLastTwoWeeks = models.BooleanField(null=True)
    hadContactLastTwoWeeks = models.BooleanField(null=True)


    




