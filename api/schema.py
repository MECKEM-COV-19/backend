

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
    users = graphene.List(Patient)
    dailyDataForPatient = graphene.List(DailyData)

    def resolve_dailyDataForPatient(self,info)
        patient = CustomUser.objects.filter(patientID=info)

    def resolve_users(self, info):
        return CustomUser.objects.all()

schema = graphene.Schema(query=Query)