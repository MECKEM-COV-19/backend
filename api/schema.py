

from graphene_django import DjangoObjectType
import graphene
from django.shortcuts import get_object_or_404

from users.models import CustomUser
from database.models import EntryData, DailyData

class PatientType(DjangoObjectType):
    class Meta:
        model = CustomUser
        description = 'Returns all Patients and their Patient IDs. You can use the Patient Id for further queries'

class EntryDataType(DjangoObjectType):
    class Meta:
        model = EntryData
        description = 'Is the regulary '

class DailyDataType(DjangoObjectType):
    class Meta:
        model = DailyData
        description = ''

class Query(graphene.ObjectType):
    users = graphene.List(PatientType)
    dailyDataForPatient = graphene.List(DailyDataType, id=graphene.String())
    entryDataForPatient = graphene.Field(EntryDataType, id=graphene.String())
    patientsWithFever = graphene.List(PatientType, temperature=graphene.Float())


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
        info="hallo123"
        patients = []
        daily = DailyData.objects.filter(temperature__gte=temp)
        for data in daily:
            patients.append(data.patient)
        return patients
    def resolve_patientsDataOverTime(self, info , **kwargs):
        time = kwargs.get('time')



    def resolve_users(self, info):
        return CustomUser.objects.all() 

schema = graphene.Schema(query=Query)