

from graphene_django import DjangoObjectType
import graphene
from django.shortcuts import get_object_or_404

from users.models import CustomUser
from database.models import EntryData, DailyData

class PatientType(DjangoObjectType):
    class Meta:
        model = CustomUser

class EntryDataType(DjangoObjectType):
    class Meta:
        model = EntryData

class DailyDataType(DjangoObjectType):
    class Meta:
        model = DailyData

class Query(graphene.ObjectType):
    users = graphene.List(PatientType)
    dailyDataForPatient = graphene.List(DailyDataType, id=graphene.String())
    entryDataForPatient = graphene.List(EntryDataType, id=graphene.String())


    def resolve_dailyDataForPatient(self,info, **kwargs):
        id= kwargs.get('id')
        print(id)
        patient = get_object_or_404(CustomUser,patientId=id)
        dailydata = DailyData.objects.filter(patient=patient)
        return dailydata

    def resolve_entryDataForPatient(self,info,**kwargs):
        id= kwargs.get('id')
        patient = get_object_or_404(CustomUser,patientId=id)
        entrydata = EntryData.objects.filter(patient=patient)
        return entrydata

    def resolve_users(self, info):
        return CustomUser.objects.all() 

schema = graphene.Schema(query=Query)