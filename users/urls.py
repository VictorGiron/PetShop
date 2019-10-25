from django.urls import path
from users import views


urlpatterns = [
    path('user/', views.ListCreateUser.as_view(), name='users'),
    path('user/<int:pk>/', views.RetrieveUpdateDestroyUser.as_view(), name='user'),

    path('veterinarian/', views.ListCreateVeterinarian.as_view(), name='veterinarians'),
    path('veterinarian/<int:pk>/', views.RetrieveUpdateDestroyVeterinarian.as_view(), name='veterinarian'),
]