from django.contrib import admin
from django.utils.safestring import mark_safe

from AutomobilkinAPIApp import models
from AutomobilkinAPIApp.models import AutoConcern, ModelCar, ModelCarGeneration, Car


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    readonly_fields = ["preview_photo"]

    def preview_photo(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin.site.register(AutoConcern)
admin.site.register(ModelCar)
admin.site.register(ModelCarGeneration)
admin.site.register(Car, CarAdmin)