from rest_framework import serializers
from .models import Car, Car_brand, Car_model, Plan

class Car_brandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_brand
        fields = ['name']

class Car_modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_model
        fields = ['name']

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['price']

class CarSerializer(serializers.ModelSerializer):
    # car_brand = Car_brandSerializer()
    # car_model = Car_modelSerializer()
    # plan = PlanSerializer()
    car_brand = serializers.CharField(source='car_brand.name')
    car_model = serializers.CharField(source='car_model.name')
    plan = serializers.IntegerField(source='plan.price')

    class Meta:
        model = Car
        fields = '__all__'
