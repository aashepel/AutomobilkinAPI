from rest_framework import serializers

from AutomobilkinAPIApp.models import AutoConcern, ModelCar, Car, ModelCarGeneration


class AutoConcernSeializer(serializers.ModelSerializer):
    class Meta:
        model = AutoConcern
        fields = "__all__"


class ModelCarSerializer(serializers.ModelSerializer):
    str = serializers.CharField(source='__str__', read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

    class Meta:
        model = ModelCar
        fields = "__all__"


class ModelCarGenerationSerializer(serializers.ModelSerializer):
    str = serializers.CharField(source='__str__', read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 2

    class Meta:
        model = ModelCarGeneration
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    str = serializers.CharField(source='__str__', read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3

    class Meta:
        model = Car
        fields = "__all__"
