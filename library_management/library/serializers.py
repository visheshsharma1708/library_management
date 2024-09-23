from rest_framework import serializers
from .models import User, Book, Assignment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_student', 'is_library_manager', 'roll_number']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'is_available']

class AssignmentSerializer(serializers.ModelSerializer):
    fine = serializers.ReadOnlyField(source='calculate_fine')

    class Meta:
        model = Assignment
        fields = ['id', 'student', 'book', 'assigned_date', 'returned_date', 'fine']
