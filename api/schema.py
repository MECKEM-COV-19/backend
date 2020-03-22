

from graphene_django import DjangoObjectType
import graphene
from django.shortcuts import get_object_or_404

from users.models import CustomUser
from database.models import EntryData, DailyData

import datetime

class PatientType(DjangoObjectType):
    class Meta:
        model = CustomUser
        description = 'Returns all Patients and their Patient IDs. You can use the Patient Id for further queries.'

class EntryDataType(DjangoObjectType):
    class Meta:
        model = EntryData
        description = 'Is the data a patient uploads ragulary.'

class DailyDataType(DjangoObjectType):
    class Meta:
        model = DailyData
        description = 'Is the data patient enters once and and is unlikely to change in short time.'

class Query(graphene.ObjectType):
    users = graphene.List(PatientType)
    dailyDataForPatient = graphene.List(DailyDataType, id=graphene.String())
    entryDataForPatient = graphene.Field(EntryDataType, id=graphene.String())
    patientsWithFever = graphene.List(PatientType, temperature=graphene.Float())
    patientsDataOverHours = graphene.List(PatientType, time=graphene.Int())
    patientsDataOverDays = graphene.List(PatientType, time=graphene.Int())


    def resolve_dailyDataForPatient(self,info, **kwargs):
        id= kwargs.get('id')
        patient = get_object_or_404(CustomUser,patientId=id)
        dailydata = DailyData.objects.filter(patient=patient)
        return dailydata

    def resolve_entryDataForPatient(self,info,**kwargs):
        id= kwargs.get('id')
        patient = get_object_or_404(CustomUser,patientId=id)
        entrydata = EntryData.objects.filter(patient=patient)
        return entrydata

    def resolve_patientsWithFever(self,info, **kwargs):
        temp = kwargs.get('temperature')
        patients = []
        daily = DailyData.objects.filter(temperature__gte=temp)
        for data in daily:
            patients.append(data.patient)
        return patients
    def resolve_patientsDataOverHours(self, info , **kwargs):
        time = kwargs.get('time')
        patients = CustomUser.objects.all()
        return_patients = []
        for patient in patients:
            dailydata = DailyData.objects.filter(patient=patient).order_by('timestamp')
            if dailydata:
                date1 = dailydata.first().timestamp
                date2 = dailydata.last().timestamp
                if not date1 is date2:
                    d = date2 - date1
                    if d.seconds/3600. >= time:
                        return_patients.append(patient)
           
        return return_patients
    def resolve_patientsDataOverDays(self, info , **kwargs):
        time = kwargs.get('time')
        patients = CustomUser.objects.all()
        return_patients = []
        for patient in patients:
            dailydata = DailyData.objects.filter(patient=patient).order_by('timestamp')
            if dailydata:
                date1 = dailydata.first().timestamp
                date2 = dailydata.last().timestamp
                if not date1 is date2:
                    d = date2 - date1
                    if d.days >= time:
                        return_patients.append(patient)
           
        return return_patients
            





    def resolve_users(self, info):
        return CustomUser.objects.all() 

schema = graphene.Schema(query=Query)