from djongo import models 
from django.db import models as django_models
from users.models import CustomUser
import uuid






class EntryData(models.Model):
    timestamp = django_models.DateTimeField(auto_now_add=True)
    has_disease = models.BooleanField()
    disease = models.TextField()
    height = models.IntegerField()
    weight = models.IntegerField()
    has_medication = models.BooleanField()
    medication = models.TextField()
    is_flu_vaccined = models.BooleanField() # Im Zeitraum von Okt19 bis heute

class DailyData(models.Model):
    timestamp = django_models.DateTimeField(auto_now_add=True)
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





class Patient(models.Model):
    patient_user = django_models.ForeignKey(CustomUser, on_delete=django_models.CASCADE, related_name="user_patient")
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,name="Patient ID")
    entrydata = models.EmbeddedField(model_container=EntryData)
    dailydata = models.ArrayField(model_container=DailyData)
    age = models.IntegerField(null=True)

    objects = models.DjongoManager()




