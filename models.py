from django.db import models
# Create your models here.

class product(models.Model):
    qnty = models.IntegerField()
    name = models.CharField(max_length=30)
    price = models.IntegerField()