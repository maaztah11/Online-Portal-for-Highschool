from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def create_student_profile(request):
    if request.method == 'POST':
        student_id = request.POST.get('student-id')
        student_name = request.POST.get('student-name')
        student_password = request.POST.get('student-password')
        platform_code = request.POST.get('student-platform-code')
        try:
            user = User.objects.get(username=student_name)
            student = StudentProfile.objects.filter(user=user).first()
            request.session['student_id']  = student_id
            return redirect("student-profile", platform_code=platform_code)
        except User.DoesNotExist:
            try:
                user = User.objects.create_user(username=student_name, password=student_password)
            except IntegrityError:
                messages.error(request, 'Username already taken!')
                return redirect('create-student-profile')
            platform = Platform.objects.filter(platform_code=platform_code).first()
            if platform:
                new_student_profile = StudentProfile.objects.create(student_id=student_id, user=user, platform=platform)
                request.session['student_id']  = student_id
                return redirect('student-profile', platform_code=platform_code)
                print("Successfully created!!")

    return render(request, 'student/create_student_profile.html')
def logout_student(request):
    try:
        del request.session['student_id']
    except KeyError:
        pass
    messages.info(request,'Logout successful')
    print('Logout successful')
    return redirect('create-student-profile')

def student_profile_page(request, platform_code):
    rooms = Room.objects.select_related('platform').filter(platform__platform_code=platform_code)

    if rooms.exists():
        platform_name = rooms[0].platform.platform_name
        context = {'platform': platform_name, 'rooms': rooms}
        print(f'platform_name {platform_name}')
    else:
        context = {'platform': 'No platform found'}
        print('No platform found')

    return render(request, 'student/student_profilepage.html', context)
