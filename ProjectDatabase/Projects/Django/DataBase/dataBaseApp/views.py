from django.shortcuts import render
from . import forms
# Create your views here.


def home(request):
    doctor = forms.DoctorForm()
    test = forms.TestForm()
    patient = forms.PatientForm()
    worker = forms.WorkerForm()
    return render(request, 'index.html',
                  {'doctor': doctor, 'test': test, 'patient': patient, 'worker': worker})
