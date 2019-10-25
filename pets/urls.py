from django.urls import path
from pets import views


urlpatterns = [
    # Pet Type
    path('pet_type/', views.ListCreatePetType.as_view(), name='pet_types'),
    path('pet_type/<int:pk>/', views.RetrieveUpdateDestroyPetType.as_view(), name='pet_type'),

    # Pet
    path('', views.ListCreatePet.as_view(), name='pets'),
    path('<int:pk>/', views.RetrieveUpdateDestroyPet.as_view(), name='pet'),

    # Food Type
    path('food_type/', views.ListCreateFoodType.as_view(), name='food_types'),
    path('food_type/<int:pk>/', views.RetrieveUpdateDestroyFoodType.as_view(), name='food_type'),

    # Feeding
    path('feeding/', views.ListCreateFeeding.as_view(), name='feedings'),
    path('feeding/<int:pk>/', views.RetrieveUpdateDestroyFeeding.as_view(), name='feeding'),

    # Vaccine
    path('vaccine/', views.ListCreateVaccine.as_view(), name='vaccines'),
    path('vaccine/<int:pk>/', views.RetrieveUpdateDestroyVaccine.as_view(), name='vaccine'),

    # Vaccination
    path('vaccination/', views.ListCreateVaccination.as_view(), name='vaccinations'),
    path('vaccination/<int:pk>/', views.RetrieveUpdateDestroyVaccination.as_view(), name='vaccination'),
]