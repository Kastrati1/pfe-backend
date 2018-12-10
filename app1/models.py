from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    categorie_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1, blank=True)
    image_url = models.CharField(max_length=200)


class Command(models.Model):
    user_id = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    #product_id = models.ForeignKey(
    #    Product, on_delete=models.CASCADE, default=1, blank=True)
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=40)
    product_price = models.FloatField(default=0)
    command_date = models.DateTimeField(default=datetime.now, blank=True)

'''
# Please don't use this User class anywhere! will be deleted soon!
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
'''