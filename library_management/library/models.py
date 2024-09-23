from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group, Permission
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_library_manager = models.BooleanField(default=False)
    roll_number = models.CharField(max_length=20, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Add this line to resolve the clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Add this line to resolve the clash
        blank=True
    )


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def calculate_fine(self):
        if self.returned_date:
            days_late = (self.returned_date - self.assigned_date).days - 10
            return max(0, days_late * 2)
        return 0
