from django.db import models
from django.utils import timezone


# Create your models here.

class Course (models.Model):
    nom = models.CharField(max_length=255)
    code = models.TextField(max_length=255)
    chargerCour = models.CharField(max_length=255)
    observation = models.TextField(max_length=255)

# Create your models here.
