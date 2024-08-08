from django.db import models

# Create your models here.

class products(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(null=True)





