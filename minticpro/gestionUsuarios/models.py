from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Tripulantes(models.Model):
    nombre = models.CharField(max_length=30)
    email =models.EmailField()
