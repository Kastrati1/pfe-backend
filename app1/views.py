import stripe
import json
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Product, Category, Command
from .serializers import CommandSerializer, ProductSerializer, CategorySerializer, UserSerializer, UserSerializerWithToken
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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsByCat(APIView):

    def get(self, request, format=None):
        print(request.data["name"])
        products = serializers.serialize(
            'json', Product.objects.filter(categorie_id=request.data["name"]))
        pro = str(products)
        p = pro.replace('\'', '\"')
        return Response(json.loads(p), status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def GetAllCategories(request):
    categories = serializers.serialize('json', Category.objects.all())
    cat = str(categories)
    c = cat.replace('\'', '\"')
    return Response(json.loads(c), status=status.HTTP_200_OK)


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

    def post(self, request, format=None):
        user_id = request.user.id
        if(user_id == None):
            return Response("Pas connecté", status=status.HTTP_406_NOT_ACCEPTABLE)
        product = Product.objects.filter(id=request.data['product_id'])
        stock = product[0].stock
        if(stock < int(request.data["quantity"])):
            return Response("Plus en stock", status=status.HTTP_406_NOT_ACCEPTABLE)
        price = int(product[0].price) * int(request.data["quantity"])

        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        print(settings.STRIPE_TEST_SECRET_KEY)
        val = stripe.Charge.create(
            amount=(price*100),
            currency="eur",
            source=request.data["token"])
        product.update(stock=(int(stock)-int(request.data["quantity"])))
        command = Command.objects.create_command(request.user.id,request.data["product_id"],request.data["quantity"], product[0].price)
        command.save()
        return Response(CommandSerializer(command).data, status=status.HTTP_201_CREATED)        
