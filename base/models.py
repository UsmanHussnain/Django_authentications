from django.db import models
from  django.contrib.auth.models import AbstractUser

# Create your models here.
    
class User(AbstractUser):
    
    email = models.EmailField(unique=True, null=True)
    password = models.TextField(null=True, blank=True, max_length=20)
    cnic = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField( max_length=15, null=True , blank=True)
    phone = models.CharField(max_length=15, null=True , blank=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    