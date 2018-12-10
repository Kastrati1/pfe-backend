from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, UserSerializer, UserSerializerWithToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.core import serializers
import json

# IMPORTER LES MODELS A TRAITER

# Create your views here.


# Get current user data and jwt
@csrf_exempt
@api_view(['GET'])
def current_user(request):
    print(request.user)
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


# UserList : Responsible for inscription
class UserList(APIView):

    # permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsByCat(APIView):

    def post(self, request, format=None):
        print(request.data["name"])
        products = serializers.serialize('json', Product.objects.filter(categorie_id=request.data["name"]))
        #print(products)
        pro = str(products)
        p = pro.replace('\'', '\"')
        return Response(json.loads(p), status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def GetAllCategories(request):
    categories = serializers.serialize('json', Category.objects.all())
    #PARSING PROBLEM
    cat = str(categories)
    c = cat.replace('\'', '\"')
    return Response(json.loads(c), status=status.HTTP_200_OK)

# returns all products


class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductsByCatViewSet(viewsets.ModelViewSet):

#     def get(self):
#         queryset = Product.objects.filter(categorie_id=self.request.data["name"])
#         serializer_class = ProductSerializer