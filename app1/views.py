
import stripe
import json
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Product, Category, Command
<<<<<<< HEAD
from .serializers import ProductSerializer, CategorySerializer, UserSerializer, UserSerializerWithToken, CommandSerializer
=======
from .serializers import CommandSerializer, ProductSerializer, CategorySerializer, UserSerializer, UserSerializerWithToken
>>>>>>> f11fa4d02890dd3b752314e50e4f0ec8682acd1e
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.core import serializers
from django.conf import settings

# Create your views here.


# Get current user data and jwt
@csrf_exempt
@api_view(['GET'])
def Current_user(request):
    print(request.user)
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


# UserList : Responsible for inscription
class UserList(APIView):

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        print(serializer)
        #print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsByCat(APIView):

    def get(self, request, format=None):
        print(request.data["name"])
        products = serializers.serialize(
            'json', Product.objects.filter(categorie_id=request.data["name"]))
        # print(products)
        pro = str(products)
        p = pro.replace('\'', '\"')
        return Response(json.loads(p), status=status.HTTP_200_OK)

'''
@csrf_exempt
@api_view(['GET'])
def GetProductsByCategory(request):
    category = CategorySerializer(data=request.data)
    products = Product.objects.filter(categorie_id__name=category.name)
    return Response(serializer.products, status=status.HTTP_200_OK)
'''

@csrf_exempt
@api_view(['GET'])
def GetAllCategories(request):
    categories = serializers.serialize('json', Category.objects.all())
    cat = str(categories)
    c = cat.replace('\'', '\"')
    return Response(json.loads(c), status=status.HTTP_200_OK)

# returns all products


class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def GetUserProducts(request):
    commands = Command.objects.filter(user_id=request.user.id)
    products = []
    commands_list = list(commands)
    for comm in commands_list:
        prod = Product.objects.get(id = comm.product_id)
        products.append(prod)
    prodSer = serializers.serialize('json', products)
    pro = str(prodSer)  
    p = pro.replace('\'', '\"')
    return Response(json.loads(p), status=status.HTTP_200_OK)


class StripeView(APIView):

    def post(self, request, format=None):  # new

        # 1 verif stock du produit si oui next, sinon error
        product = Product.objects.filter(id=request.data['product_id'])
        stock = product[0].stock
        if(stock == 0):
            return Response("Plus en stock", status=status.HTTP_406_NOT_ACCEPTABLE)
        price = int(product[0].price)
        print(price *100)
        
        # faire payment par stripe si oui next, sinon error
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        print(settings.STRIPE_TEST_SECRET_KEY)
        val = stripe.Charge.create(
            amount=(price*100),
            currency="eur",
            source=request.data["token"])
        #Pas besoin de tester val, stripe renvoi erreur en cas de refus
        
        # enregistrer dans la db si oui next, sinon errror
        #TODO jwt, id_product, stripe token (Authorization)
        product = Product.objects.filter(id = request.data["product_id"])
        command = Command.objects.create_command(request.user.id,request.data["product_id"],request.data["quantity"], product[0].price)
        command.save()
        return Response(CommandSerializer(command).data, status=status.HTTP_201_CREATED)        
