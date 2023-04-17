from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from AutomobilkinAPIApp.models import AutoConcern, ModelCar, ModelCarGeneration, Car
from AutomobilkinAPIApp.serializers import AutoConcernSeializer, ModelCarSerializer, ModelCarGenerationSerializer, \
    CarSerializer


# Create your views here.

class AutoConcernViewSet(viewsets.ModelViewSet):
    queryset = AutoConcern.objects.all()
    serializer_class = AutoConcernSeializer


class ModelCarViewSet(viewsets.ModelViewSet):
    queryset = ModelCar.objects.all()
    serializer_class = ModelCarSerializer


class ModelCarGenerationViewSet(viewsets.ModelViewSet):
    queryset = ModelCarGeneration.objects.all()
    serializer_class = ModelCarGenerationSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
