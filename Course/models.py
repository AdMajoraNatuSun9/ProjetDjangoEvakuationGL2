from django.db import models
from django.utils import timezone


# Create your models here.

class Teacher (models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.TextField(max_length=255)

# Create your models here.
