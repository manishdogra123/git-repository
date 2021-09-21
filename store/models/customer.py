from django.db import models



class customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=5000)
