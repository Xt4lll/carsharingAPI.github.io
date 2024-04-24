from django.db import models
from django.core.validators import MaxValueValidator

class Car_brand(models.Model):
    name = models.CharField(max_length=25, verbose_name='марка авто')

    def __str__(self):
        return self.name
    
class Car_model(models.Model):
    name = models.CharField(max_length=25, verbose_name='модель авто')

    def __str__(self):
        return self.name
    

class Plan(models.Model):
    price = models.IntegerField(verbose_name='стоимость минуты поездки')

    def __str__(self):
        return str(self.price)


class Car(models.Model):
    number = models.CharField(max_length=6, verbose_name='номер авто')
    fuel = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='количество топлива')
    latitude = models.DecimalField(max_digits=8, decimal_places=6, verbose_name='широта')
    longitude = models.DecimalField(max_digits=8, decimal_places=6, verbose_name='долгота')
    is_available = models.BooleanField(verbose_name='доступна?')

    car_brand = models.ForeignKey(Car_brand, verbose_name='марка авто', on_delete=models.CASCADE, null=True)
    car_model = models.ForeignKey(Car_model, verbose_name='модель авто', on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(Plan, verbose_name='тариф', on_delete=models.CASCADE, null=True)   