import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


class CustomUser(AbstractBaseUser):

    user_code = models.CharField('code', max_length=100, primary_key=True)

    def save(self, data, *args, **kwargs):
        print(data)

        if data:
            # Generate user_code without altering the original data dictionary
            user_code = self.custom_hash(data.copy())
            print(user_code)
            try:
                user = CustomUser.objects.get(user_code=user_code)
            except CustomUser.DoesNotExist:
                user = None

            if user:
                return

            print(data, user)
            self.user_code = user_code
        else:
            raise ValueError("Data must be provided")

        super().save(*args, **kwargs)

    def custom_hash(self, data):

        print(data,4)

        initial_key = Fernet.generate_key()
        cipher = Fernet(initial_key)

        encrypted_data = {}
        for key, value in data.items():
            encrypted = cipher.encrypt(value.encode())
            encrypted_data[key] = encrypted

            new_key = self.generate_key_from_hash(encrypted)
            cipher = Fernet(new_key)

        combined_encrypted_data = b" ".join(encrypted_data.values())
        return str(combined_encrypted_data)

    def generate_key_from_hash(self, input_key):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'some_salt',
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(input_key))

    def __str__(self):
        return self.user_code

class MedicalData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='medical_data')

    class Gender(models.TextChoices):
        MALE = 'Male', 'Man'
        FEMALE = 'Female', 'Woman'

    class Continent(models.TextChoices):
        ASIA = 'ASIA', 'Asia'
        EUROPE = 'EUROPE', 'Europe'
        AFRICA = 'AFRICA', 'Africa'
        NORTH_AMERICA = 'North America', 'North America'
        SOUTH_AMERICA = 'South America', 'South America'
        AUSTRALIA = 'Australia', 'Australia'

    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.MALE)

    WBC = models.FloatField()  # White Blood Cells
    RBC = models.FloatField()  # Red Blood Cells
    HGB = models.FloatField()  # Hemoglobin
    HCT = models.FloatField()  # Hematocrit
    MCV = models.FloatField()  # Mean Corpuscular Volume
    MCH = models.FloatField()  # Mean Corpuscular Hemoglobin
    MCHC = models.FloatField()  # Mean Corpuscular Hemoglobin Concentration
    RDW = models.FloatField()  # Red Cell Distribution Width
    PLT = models.FloatField()  # Platelets
    MPV = models.FloatField()  # Mean Platelet Volume
    Neutrophils = models.FloatField()
    Lymphocytes = models.FloatField()
    Monocytes = models.FloatField()
    Eosinophils = models.FloatField()
    Basophils = models.FloatField()
    Glucose = models.FloatField()
    Urea = models.FloatField()
    Creatinine = models.FloatField()
    Cholesterol = models.FloatField()
    HDL = models.FloatField()  # High-Density Lipoprotein
    LDL = models.FloatField()  # Low-Density Lipoprotein
    Triglycerides = models.FloatField()
    ALT = models.FloatField()  # Alanine Aminotransferase
    AST = models.FloatField()  # Aspartate Aminotransferase
    Bilirubin = models.FloatField()
    Total_Protein = models.FloatField()
    Albumin = models.FloatField()
    Globulin = models.FloatField()
    Calcium = models.FloatField()
    Phosphorus = models.FloatField()
    Magnesium = models.FloatField()
    Sodium = models.FloatField()
    Potassium = models.FloatField()
    Chloride = models.FloatField()

    Continent = models.CharField(max_length=13, choices=Continent.choices, default=Continent.ASIA)
    Capital = models.CharField(max_length=100)

