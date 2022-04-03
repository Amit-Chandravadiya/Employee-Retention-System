from pyexpat import model
from django.db import models

# Create your models here.

class ContactDetails(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField(max_length=500)
    def __str__(self):
	    return self.name