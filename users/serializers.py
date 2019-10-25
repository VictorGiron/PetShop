from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import User, Veterinarian
from pets.models import PetType, Pet, Feeding, Vaccination


# Intermediate Serializers
class PetTypeSerializer(ModelSerializer):
    class Meta:
        model = PetType
        fields = '__all__'


class FeedingSerializer(ModelSerializer):
    class Meta:
        model = Feeding
        fields = ['id', 'name', 'type', 'time']
        depth = 1


class VaccinationSerializer(ModelSerializer):
    class Meta:
        model = Vaccination
        fields = ['id', 'vaccine']
        depth = 1


class OwnerPetSerializer(ModelSerializer):
    type = PetTypeSerializer()
    feedings = FeedingSerializer(source='feeding_set', many=True)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'type', 'birth_date', 'feedings']


class VeterinarianPetSerializer(ModelSerializer):
    type = PetTypeSerializer()
    vaccinations = VaccinationSerializer(source='vaccination_set', many=True)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'type', 'birth_date', 'vaccinations']


# User
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(ModelSerializer):
    pets = OwnerPetSerializer(source='pet_set', many=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'birth_date', 'pets']


# Veterinarian
class VeterinarianSerializer(ModelSerializer):
    class Meta:
        model = Veterinarian
        fields = '__all__'


class VeterinarianDetailSerializer(ModelSerializer):
    pets = SerializerMethodField()

    class Meta:
        model = Veterinarian
        fields = ['id', 'name', 'email', 'birth_date', 'pets']

    def get_pets(self, veterinarian):

        vaccinations = veterinarian.vaccination_set.all()

        pets = {vaccination.pet for vaccination in vaccinations}

        return VeterinarianPetSerializer(instance=pets, many=True).data