from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class Custom_user(AbstractUser):
    username = None
    email = models.EmailField(max_length=254 , unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100 , blank=True , null = True)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_inspector = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    inspector_id = models.CharField(max_length=20,null = True, blank=True)
    inspector_dept = models.CharField(max_length=100,null = True, blank=True)
    inspector_desig = models.CharField(max_length=100,null = True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return f"user is {self.email} with id {str(self.id)}"
    
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(Custom_user, on_delete=models.CASCADE)
    dob = models.CharField(max_length=15,null = True, blank=True)
    phone = models.CharField(max_length=15,null = True, blank=True)
    gender = models.CharField(max_length=10,null = True, blank=True)
    address = models.TextField(null = True, blank=True)
    emergency_contact = models.CharField(max_length=15,null = True, blank=True)
