from django.db import models

class Enseignant(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    