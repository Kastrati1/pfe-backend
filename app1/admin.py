from django.contrib import admin
from .models import Product, User, Categorie, Command


# Register your models here.

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Command)
