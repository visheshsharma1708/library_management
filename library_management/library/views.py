from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import User, Book, Assignment
from .serializers import UserSerializer, BookSerializer, AssignmentSerializer
from django.shortcuts import render
def home(request):
    return render(request, 'library/index.html, context={}')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin can perform CRUD operations on users

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

    def list(self, request, *args, **kwargs):
        if request.query_params.get('available') == 'true':
            self.queryset = self.queryset.filter(is_available=True)
        if request.query_params.get('available') == 'false':
            self.queryset = self.queryset.filter(is_available=False)
        return super().list(request, *args, **kwargs)

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_student:
            serializer.save(student=self.request.user)
        elif self.request.user.is_library_manager:
            roll_number = self.request.data.get('roll_number')
            student = User.objects.filter(roll_number=roll_number, is_student=True).first()
            if student:
                serializer.save(student=student)

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.returned_date:
            instance.fine = instance.calculate_fine()
            instance.save()

class AcceptFineViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        roll_number = request.data.get('roll_number')
        student = User.objects.filter(roll_number=roll_number, is_student=True).first()
        if student and request.user.is_library_manager:
            # Accept the fine logic here
            return Response({"message": "Fine accepted"}, status=status.HTTP_200_OK)
        return Response({"error": "Unauthorized"}, status=status.HTTP_400_BAD_REQUEST)
