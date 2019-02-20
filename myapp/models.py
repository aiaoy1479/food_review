from django.db import models
from django.utils import timezone

class Review(models.Model):
    title = models.TextField(max_length=100)
    rating = models.IntegerField(default=0)
    writer_name = models.CharField(max_length=50)
    body = models.TextField(max_length=600)
    review_date = models.DateTimeField('date published')

class Cate(models.Model):
    shop_cate = models.TextField(max_length=50)
    food_cate = models.TextField(max_length=50)

class Menu(models.Model):
    menu = models.TextField(max_length=50)
    cost = models.IntegerField(default=0)

class Shop(models.Model):
    name = models.TextField(max_length=100)
    locate = models.TextField(max_length=100)
    note = models.TextField(max_length=200)
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

