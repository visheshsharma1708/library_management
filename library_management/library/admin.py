from django.contrib import admin
from .models import User, Book, Assignment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'is_student', 'is_library_manager', 'roll_number')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_available']

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'book', 'assigned_date', 'returned_date', 'fine']
