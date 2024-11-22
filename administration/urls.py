from django.urls import path
from administration import views
urlpatterns = [
    path('',views.index, name='index'),
    path('register_admin/', views.register_admin,name='register-admin'),
    path('add_organization/<str:username>/',views.add_organization,name='add-organization'),
    path('admin_dashboard/<str:platform_name>/', views.admin_dashboard, name='admin-dashboard'),
    path('admin-logout/', views.admin_logout,name='admin-logout')
]