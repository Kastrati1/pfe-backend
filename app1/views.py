from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Product, User
from .serializers import ProductSerializer, UserSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

#IMPORTER LES MODELS A TRAITER

# Create your views here.


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@csrf_exempt
@api_view(['POST'])
def Inscription(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            #INSERT
            #serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #FAIL
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def GetProducts(request):
    if request.method == "GET":
        products = Product.objects.all()
        for p in products:
            print(p)
        return Response(serializer.products, status=status.HTTP_200_OK)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)