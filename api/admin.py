from django.contrib import admin
from .models import *

@admin.register(Car_brand)
class Car_brandAdmin(admin.ModelAdmin):
    display = 'name'

@admin.register(Car_model)
class Car_modelAdmin(admin.ModelAdmin):
    display = 'name'

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    display = 'price'

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('number', 'fuel', 'latitude', 'longitude'
                    , 'is_available', 'car_brand', 'car_model', 'plan')