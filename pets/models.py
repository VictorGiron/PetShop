from django.db import models
from users.models import User, Veterinarian


# Create your models here.
class PetType(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=25)
    type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField()

    def __str__(self):
        return self.name + ' (' + self.type.name + ')'


class FoodType(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Feeding(models.Model):
    name = models.CharField(max_length=25)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return self.pet.name + ' - ' + self.name + ' (' + str(self.time) + ')'


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)