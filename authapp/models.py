from django.db import models

# Create your models here.
class User(models.Model) :
    username = models.CharField(max_length = 100, default="appuser")
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 1000)

