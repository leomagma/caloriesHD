from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

class User(AbstractUser):
    
    email = models.EmailField(max_length=200,unique=True)
    daily_calo = models.IntegerField(null=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('username','password','daily_calo')

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def __str__(self):
        return (self.username)
    
    
"""class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    password = models.CharField(max_length=50)
    daily_Calo = models.IntegerField()
    
    def __str__(self) -> str:
        return self.username
    """