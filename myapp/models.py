from django.db import models
from django.utils import timezone

class Review(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    writer_name = models.CharField(max_length=50)
    body = models.CharField(max_length=600)
    review_date = models.DateTimeField('date published')

class Cate(models.Model):
    shop_cate = models.CharField(max_length=50)
    food_cate = models.CharField(max_length=50)

class Menu(models.Model):
    menu = models.CharField(max_length=50)
    cost = models.IntegerField()

class Shop(models.Model):
    name = models.CharField(max_length=100)
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    locate = models.CharField(max_length=100)
    note = models.CharField(max_length=200)

