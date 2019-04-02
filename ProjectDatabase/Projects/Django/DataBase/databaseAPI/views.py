from . import serializers
from dataBaseApp import models
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def api_home_view(request):
    return HttpResponse("<h2>API view.</h2>")


class CreateDoctor(generics.ListCreateAPIView):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
