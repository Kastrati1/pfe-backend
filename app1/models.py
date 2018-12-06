from django.db import models

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.IntegerField()
    categorie_id = models.ForeignKey(Categorie,on_delete=models.CASCADE)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Commande(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=40)


