from django.urls import path
from teachers import views

urlpatterns = [
    path('create_teacher_profile/', views.create_teacher_profile, name='create-teacher-profile'),
    path('create_room/',views.create_room, name='create-room'),
    path('teacher_logout/', views.logout_teacher, name='teacher-logout'),
    path('room_view/<str:room_name>/<str:teacher_name>/', views.room_view, name='room-view'),
    path('manage_assignments/<str:room_name>/<str:teacher_name>/', views.manage_assignments, name='manage-assignments'),
    path('delete_assignment/<int:assignment_id>/', views.delete_assignment, name='delete-assignment')
]