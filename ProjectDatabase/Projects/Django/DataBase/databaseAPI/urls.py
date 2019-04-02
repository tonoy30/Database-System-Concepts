from django.urls import path
from databaseAPI import views

urlpatterns = [
    path('', views.api_home_view, name='api_home'),
    path('doctor/', views.CreateDoctor.as_view(), name='doctor'),
]
