from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=20)


class Client(models.Model):
    name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=20)
    user = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE, through='Order')


class Worker(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    user = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE, through='Order')


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField()


class Food(models.Model):
    name = models.CharField(max_length=20)
    start_price = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients', through='Order')

    def food_price(self, *args, **kwargs):
        if self.ingredients:
            return self.start_price + self.ingredients.extra_price
        return self.start_price

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='foods')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name='ingredients')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='clients')
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT, related_name='workers')
    order_date_time = models.DateTimeField(default=timezone.now)

