from django.shortcuts import render
from rest_framework import viewsets
from .serilizers import CarSerilizer
from .models import Car
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CarAPI(viewsets.ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerilizer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]