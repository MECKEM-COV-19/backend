

from graphene_django import DjangoObjectType
import graphene
from users.models import CustomUser
from database.models import EntryData, DailyData

class Patient(DjangoObjectType):
    class Meta:
        model = CustomUser

class Query(graphene.ObjectType):
    users = graphene.List(Patient)

    def resolve_users(self, info):
        return CustomUser.objects.all()

schema = graphene.Schema(query=Query)