# Djang and 3rd party Imports
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.
class ContactUs(models.Model):
    """
    Class for our contact model
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField(null=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Contacting request from {self.name}"