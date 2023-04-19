from django.db.models import Sum
from django.shortcuts import render
from rest_framework import viewsets, generics, status, serializers
from rest_framework.decorators import api_view, action
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

    @action(detail=False, methods=["get"], url_path=r'SumCars')
    def get_sum_all_cars(self, request):
        sum = self.queryset.aggregate(Sum('price_rubles'))
        return Response(sum, status=status.HTTP_200_OK)
