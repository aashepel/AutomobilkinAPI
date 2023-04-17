from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class AutoConcern(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ModelCar(models.Model):
    auto_concern = models.ForeignKey('AutoConcern', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.auto_concern.title} {self.model_name}'


class ModelCarGeneration(models.Model):
    model_car = models.ForeignKey('ModelCar', on_delete=models.CASCADE)
    year_start_release = models.IntegerField()
    year_finish_release = models.IntegerField()
    generation = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.model_car} - {self.generation}'


class Car(models.Model):
    class Body(models.TextChoices):
        SEDAN = 'SEDAN', _('Седан')
        HATCHBACK = 'HATCHBACK', _('Хетчбек')
        LIFTBACK = 'LIFTBACK', _('Лифтбек')
        SUV = 'SUV', _('Внедорожник')

    class TransmissionType(models.TextChoices):
        AUTOMATIC = 'AUTOMATIC', _('Автоматическая')
        ROBOTIC = 'ROBOTIC', _('Роботизированная')
        MECHANIC = 'MECHANIC', _('Механическая')
        VARIATOR = 'VARIATOR', _('Вариатор')

    class EngineType(models.TextChoices):
        GASOLINE = 'GASOLINE', _('Бензиновый')
        DISEL = 'DISEL', _('Дизельный')
        HYBRID = 'HYBRID', _('Гибридный')
        ELECTIRC = 'ELECTIRC', _('Электрический')

    class DriveType(models.TextChoices):
        REAR = 'REAR', _('Задний')
        FRONT = 'FRONT', _('Передний')
        FULL = 'FULL', _('Полный')

    class SteeringWheel(models.TextChoices):
        LEFT = 'LEFT', _('Левый')
        RIGHT = 'RIGHT', _('Правый')

    model_car_generation = models.ForeignKey('ModelCarGeneration', on_delete=models.CASCADE)
    is_new = models.BooleanField()
    body_type = models.CharField(choices=Body.choices, max_length=9)
    transmission_type = models.CharField(choices=TransmissionType.choices, max_length=9)
    engine_type = models.CharField(choices=EngineType.choices, max_length=8)
    engine_volume = models.FloatField()
    engine_power = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    drive_type = models.CharField(choices=DriveType.choices, max_length=5)
    year_of_release = models.IntegerField()
    odometer = models.IntegerField()
    price_rubles = models.IntegerField()
    color = models.CharField(max_length=100)
    count_owners = models.IntegerField()
    steering_wheel_type = models.CharField(choices=SteeringWheel.choices, max_length=5)
    vin_code = models.CharField(max_length=17)
    state_number = models.CharField(max_length=9)
    image = models.ImageField(upload_to='photos/', blank=True, )

    def __str__(self):
        return f'{self.model_car_generation} - {self.year_of_release} | {self.engine_volume} л. - {self.engine_power} л.с | {self.color}'