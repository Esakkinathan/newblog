from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.utils import timezone
import datetime

class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return self.created_at >= timezone.now() - datetime.timedelta(minutes=10)

class CustomUser(AbstractUser):
    email =     models.EmailField(max_length=100,unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']