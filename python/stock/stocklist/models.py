from django.db import models

# Create your models here.
class Stock(models.Model):
    stockcode = models.CharField(max_length=20) 
    stockname = models.CharField(max_length=20)