from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from users.models import User, Veterinarian
from users.serializers import UserSerializer, UserDetailSerializer, VeterinarianSerializer, VeterinarianDetailSerializer


# Create your views here.
class ListCreateUser(ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserDetailSerializer
        elif self.request.method == 'POST':
            return UserSerializer


class RetrieveUpdateDestroyUser(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return UserSerializer


# Create your views here.
class ListCreateVeterinarian(ListCreateAPIView):
    queryset = Veterinarian.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VeterinarianDetailSerializer
        elif self.request.method == 'POST':
            return VeterinarianSerializer


class RetrieveUpdateDestroyVeterinarian(RetrieveUpdateDestroyAPIView):
    queryset = Veterinarian.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VeterinarianDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return VeterinarianSerializer
