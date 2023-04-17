from rest_framework import serializers

from AutomobilkinAPIApp.models import AutoConcern, ModelCar, Car, ModelCarGeneration


class AutoConcernSeializer(serializers.ModelSerializer):
    class Meta:
        model = AutoConcern
        fields = "__all__"


class ModelCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelCar
        fields = "__all__"


class ModelCarGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelCarGeneration
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
