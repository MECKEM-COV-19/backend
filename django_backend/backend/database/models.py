
from django.db import models
from users.models import CustomUser
import uuid

import datetime




class EntryData(models.Model):
    patient = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="entry_data")
    timestamp = models.DateField(default=datetime.date.today().strftime("%d-%m-%Y"))
    has_disease = models.BooleanField()
    disease = models.TextField()
    height = models.IntegerField()
    weight = models.IntegerField()
    has_medication = models.BooleanField()
    medication = models.TextField()
    is_flu_vaccined = models.BooleanField() # Im Zeitraum von Okt19 bis heute
    age = models.IntegerField(null=True)
    gender = models.IntegerField(choices=(("1","male"),("2","female"),("3","divers")))


class DailyData(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="daily_data")
    timestamp = models.DateField(input_formats=['%d-%m-%Y'],default=datetime.date.today().strftime("%d-%m-%Y"))
    is_covid_positive = models.BooleanField()
    temperature = models.FloatField()
    has_chills = models.BooleanField()
    is_feeling_weak = models.BooleanField()
    has_body_aches = models.BooleanField()
    has_continous_cough = models.BooleanField()
    has_sniff = models.BooleanField()
    has_diarrhea = models.BooleanField()
    has_throat_pain = models.BooleanField()
    has_headache = models.BooleanField()
    is_easier_out_of_breath = models.BooleanField()
    was_riskzone_last_two_weeks = models.BooleanField()
    had_contact_last_two_weeks = models.BooleanField()


    




