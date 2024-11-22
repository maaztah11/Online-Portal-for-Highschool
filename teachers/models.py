from django.db import models
from django.contrib.auth.models import User
from administration.models import Platform

# Create your models here.
class TeacherProfile(models.Model):
    teacher_name = models.CharField(max_length=50, unique=False)
    teacher_subject = models.CharField(max_length=50, unique=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
class Room(models.Model):
    room_name = models.CharField(max_length=10)
    room_code = models.CharField(max_length=5)
    teacher = models.OneToOneField(TeacherProfile, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.room_name
class Assignment(models.Model):
    grade_choices = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D')
    )
    assignment_title = models.CharField(max_length=30)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    uploaded_by = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, null=True)
    assignment_file = models.FileField(upload_to='assignments', null=True)
    grade = models.CharField(choices=grade_choices, default='Null', max_length=10)
    def __str__(self):
        return self.assignment_title