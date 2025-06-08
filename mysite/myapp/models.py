from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    carbs=models.FloatField(default=0)
    protein=models.FloatField(default=0)
    fats=models.FloatField(default=0)
    calorie=models.IntegerField(default=0)
    fibre=models.FloatField(default=0)
    sugar=models.FloatField(default=0)


class Consume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food,on_delete=models.CASCADE)


