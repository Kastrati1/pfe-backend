from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Product
from django.contrib.auth.models import User
from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView

# IMPORTER LES MODELS A TRAITER

# Create your views here.


# class GetAllProducts(CAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


@csrf_exempt
@api_view(['GET'])
def GetProducts(request):
    if request.method == "GET":
        serializer = ProductSerializer()
        queryset = Product.objects.all()
        for p in queryset:
            print(p)
            serializer = ProductSerializer(p)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
