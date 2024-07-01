from django.db import models
from  django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

# Create your models here.
    
class User(AbstractUser):
    
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, null=True)
    password = models.TextField(null=True, blank=True, max_length=20)
    cnic = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField( max_length=15, null=True , blank=True)
    phone = models.CharField(max_length=15, null=True , blank=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def generate_verification_token(self):
        token = get_random_string(length=32)
        self.verification_token = token
        self.save()
        return token
    
    def __str__(self):
        return self.email
    
    