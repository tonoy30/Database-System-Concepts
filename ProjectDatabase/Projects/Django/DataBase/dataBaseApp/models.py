from django.db import models
import uuid
from .functions import gen_random
# Create your models here.


class Doctor(models.Model):
    doctor_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=14, null=False)
    designation = models.CharField(max_length=100)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Test(models.Model):
    test_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    test_name = models.CharField(max_length=30, default="Test")
    test_price = models.DecimalField(max_digits=5, decimal_places=2)
    test_type = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    normal_value = models.DecimalField(max_digits=5, decimal_places=2)
    upto_value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.test_name


class Patient(models.Model):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

    GENDER_CHOICE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )

    patient_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    patient_name = models.CharField(max_length=30)
    patient_gender = models.CharField(
        max_length=1, choices=GENDER_CHOICE, default=FEMALE)
    patient_age = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=14, null=False)
    test_name = models.ForeignKey(Test, on_delete=models.CASCADE)
    ref_by = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    speciman_type = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.patient_name


class Worker(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14, null=False, unique=True)
    address = models.TextField(max_length=1024*2)

    def __str__(self):
        return self.name


class Report(models.Model):
    id = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    ref_by = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    speciman_type = models.CharField(max_length=20)
    tests = models.ForeignKey(Test, on_delete=models.CASCADE)
    worker = models.OneToOneField(
        Worker, on_delete=models.CASCADE, primary_key=True)
    test_report = models.TextField()

    def __str__(self):
        return str(self.id)


class CashMemo(models.Model):
    bill_no = models.CharField(
        max_length=10, default="MMC{0}".format(gen_random(4)))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    delivary_date_time = models.DateTimeField()

    def __str__(self):
        return self.bill_no
