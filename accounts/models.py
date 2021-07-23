from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    token = models.CharField(max_length=150,null=True,blank=True)
    verify = models.BooleanField(default=False,null=True,blank=True)

    PhoneNumber = PhoneNumberField()


