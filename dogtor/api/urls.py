from django.urls import path, include
from rest_framework import routers

# Views
from .views import ListOwnersAPIView, RetrieveOwnerAPIView, CreateOwnerAPIView, UpdateOwnerAPIView, DeleteOwnerAPIView

# Routers se usa para juntar todo en un solo recurso hacer todo el CRUD
# router = routers.DefaultRouter()
# router.register(r"owners", OwnersViewSet)
# router.register(r"pets", PetsViewSet)
# router.register(r"pet-dates", PetDatesViewSet)

urlpatterns = [
  # path("", include(router.urls)),
  path("owners/", ListOwnersAPIView.as_view(), name="owners_list"),
  path("owners/<int:pk>/", RetrieveOwnerAPIView.as_view(), name="owner_detail"),
  path("owners/<int:pk>/add/", CreateOwnerAPIView.as_view(), name="owner_detail"),
  path("owners/<int:pk>/update/", UpdateOwnerAPIView.as_view(), name="owner_detail"),
  path("owners/<int:pk>/delete/", DeleteOwnerAPIView.as_view(), name="owner_detail"),
 ]
