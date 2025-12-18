from django.db import models

# Create your models here.
class Carro(models.Model): # car model added
    title = models.TextField(max_length=255)