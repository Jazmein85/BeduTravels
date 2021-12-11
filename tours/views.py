from django.contrib.auth import views
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets, serializers 
from tours.models import Tour, Zona, User

# Create your views here.
from tours.models import Tour
from django.contrib.auth.decorators import login_required

from .models import Zona, Tour

@login_required()
def index(request):
    """ Vista para atender la petición de la url / """
    # Obteniendo los datos mediantes consultas
    tours = Tour.objects.all()
    zonas = Zona.objects.all()

    return render(request, "index.html", {"tours":tours, "zonas":zonas})

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """

    class Meta:
        # Se define sobre que modelo actua
        model = User
        # Se definen los campos a incluir
        fields = ('id', 'name', 'last_name', 'email', 'birthday', 'gender', 'key', 'type')


class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """

    class Meta:
        # Se define sobre que modelo actua
        model = Zona
        # Se definen los campos a incluir
        fields = ('nombre', 'descripcion', 'latitud', 'longitud','tours_salida', 'tours_llegada')

class TourSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para User """

    class Meta:
        # Se define sobre que modelo actua
        model = Tour
        # Se definen los campos a incluir
        fields = ('name', 'operator', 'img')


class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all().order_by('id')

    serializer_class = UserSerializer

class ZonaViewSet(viewsets.ModelViewSet):
    queryset =Zona.objects.all().order_by('id')

    serializer_class = ZonaSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset =Tour.objects.all().order_by('id')

    serializer_class = TourSerializer


