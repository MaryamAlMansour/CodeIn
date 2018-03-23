from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    developer = models.BooleanField(default=False)
    python = models.BooleanField(default=False)
    java = models.BooleanField(default=False)
    standard_c = models.BooleanField(default=False)
    c_plus_plus = models.BooleanField(default=False)
    other_language = models.CharField(max_length=12)


    
