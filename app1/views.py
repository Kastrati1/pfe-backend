from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Product, User
from .serializers import ProductSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

#IMPORTER LES MODELS A TRAITER

# Create your views here.


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST'])
def Inscription(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            #INSERT
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #FAIL
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)