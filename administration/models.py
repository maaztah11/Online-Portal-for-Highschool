from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Role_choices = (
        ('Admin', 'admin'),
        ('Teacher', 'teacher'),
        ('Student', 'student')
    )
    role = models.CharField(max_length=15, choices=Role_choices)
class Platform(models.Model):
    platform_name = models.CharField(max_length=10)
    platform_code = models.CharField(max_length=6)
    admin = models.OneToOneField(Organization_Admin, on_delete=models.CASCADE)

