from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=40)

class User(models.Model):
    #TEMPLATE
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
