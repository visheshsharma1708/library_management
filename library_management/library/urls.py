from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, AssignmentViewSet, AcceptFineViewSet, home  # Import the home view correctly

# Define the router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'accept-fine', AcceptFineViewSet, basename='accept-fine')

# Combine the urlpatterns
urlpatterns = [
    path('home/', home),  # Route for the home view
    path('api/', include(router.urls)),  # API routes using the router
]
