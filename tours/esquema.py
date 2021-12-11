from graphene_django import DjangoObjectType
from graphene_django.types import DjangoObjectTypeOptions
from tours.models import User, Zona
import graphene



class UserType(DjangoObjectType):
    class Meta:
        model = User

class ZoneType(DjangoObjectType):
    class Meta:
        model = Zona

class Query(graphene.ObjectType):
    """ Definición de las respuestas a las consultas posibles """

    # Se definen los posibles campos en las consultas
    all_users = graphene.List(UserType)  # allUsers
    all_zones = graphene.List(ZoneType)  # allZonas

    # Se define las respuestas para cada campo definido
    def resolve_all_users(self, info, **kwargs):
        # Responde con la lista de todos registros
        return User.objects.all()

    def resolve_all_zonas(self, info, **kwargs):
        # Responde con la lista de todos registros
        return Zona.objects.all()

schema = graphene.Schema(query=Query)

