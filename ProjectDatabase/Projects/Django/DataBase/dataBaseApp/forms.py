from django import forms
from . import models


class DoctorForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=14)
    designation = forms.CharField(max_length=100)
    address = forms.CharField(max_length=50)


class TestForm(forms.ModelForm):
    class Meta:
        model = models.Test
        fields = ['test_name', 'test_price', 'test_type',
                  'description', 'normal_value', 'upto_value']


class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['patient_name', 'patient_gender',
                  'patient_age', 'phone_number', 'test_name',
                  'ref_by', 'address', 'speciman_type']


class WorkerForm(forms.ModelForm):
    class Meta:
        model = models.Worker
        fields = ['name', 'email', 'phone_number', 'address']
