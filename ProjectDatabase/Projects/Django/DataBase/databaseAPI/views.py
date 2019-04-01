from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def api_home_view(request):
    return HttpResponse("<h2>API view.</h2>")
