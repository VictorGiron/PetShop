from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Veterinarian(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name
