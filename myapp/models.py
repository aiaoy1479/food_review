from django.db import models
from django.utils import timezone

class Shop(models.Model):
    name = models.TextField(max_length=100)
    locate = models.TextField(max_length=100)
    note = models.TextField(default='', max_length=200)
    rating = models.FloatField(default=0)
    shop_cate = models.TextField(default='')
    food_cate = models.TextField(default='')

class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    rating = models.FloatField(default=0)
    writer_name = models.CharField(max_length=50)
    body = models.TextField(default='', max_length=600)
    review_date = models.DateTimeField(default=timezone.now)

class Menu(models.Model):
    menu = models.TextField(max_length=50)
    cost = models.IntegerField(default=0)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
