from rest_framework.serializers import ModelSerializer
from pets.models import PetType, Pet, FoodType, Feeding, Vaccine, Vaccination


# Pet Type
class PetTypeSerializer(ModelSerializer):
    class Meta:
        model = PetType
        fields = '__all__'


class PetTypeDetailSerializer(ModelSerializer):
    class Meta:
        model = PetType
        fields = ['id', 'name']


# Pet
class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class PetDetailSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'type', 'owner', 'birth_date']


# Food Type
class FoodTypeSerializer(ModelSerializer):
    class Meta:
        model = FoodType
        fields = '__all__'


# Feeding
class FeedingSerializer(ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'


class FeedingDetailSerializer(ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
        depth = 2


# Vaccine
class VaccineSerializer(ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'


# Vaccination
class VaccinationSerializer(ModelSerializer):
    class Meta:
        model = Vaccination
        fields = '__all__'