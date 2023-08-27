from django.db import models


# Create your models here.
class Project(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    projet = models.FileField()
