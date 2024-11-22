from django.urls import path
from student import views

urlpatterns = [
    path('create_student_profile/', views.create_student_profile, name='create-student-profile'),
    path('logout_student/', views.logout_student, name='logout-student'),
    path('student_profile/<str:platform_code>/', views.student_profile_page, name='student-profile')
]