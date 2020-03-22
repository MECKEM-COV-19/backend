

from graphene_django import DjangoObjectType
import graphene
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
    dailyDataForPatient = graphene.List(DailyDataType)


    def resolve_dailyDataForPatient(self,info, **kwargs):
        id= kwargs.get('patientId')
        patient = get_object_or_404(CustomUser,patientId=id)
        dailydata = DailyData.objects.filter(patient=patient)
        return dailydata

    def resolve_entryDataorPatient(self,info,**kwargs):
        pass

    def resolve_users(self, info):
        return CustomUser.objects.all()

schema = graphene.Schema(query=Query)