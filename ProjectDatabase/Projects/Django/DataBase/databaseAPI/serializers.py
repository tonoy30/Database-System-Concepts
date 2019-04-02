from rest_framework import serializers
from dataBaseApp import models


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'email',
            'phone_number',
            'designation',
            'address'
        )
        model = models.Doctor
