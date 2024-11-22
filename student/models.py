from django.db import models
from django.contrib.auth.models import User
from administration.models import Platform
from teachers.models import Room

# Create your models here.
class StudentProfile(models.Model):
    student_id = models.CharField(max_length=25)
    student_name = models.CharField(max_length=30, null=True)
    student_password = models.CharField(max_length=10, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    platform = models.OneToOneField(Platform, on_delete=models.CASCADE)
    room = models.ManyToManyField(Room, related_name='room')
    def __str__(self):
        return self.student_id
class Student_submissions(models.Model):
    assignment_file = models.FileField(upload_to='student_submissions')
    submitted_by = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)


