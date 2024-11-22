from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def create_teacher_profile(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher-name')
        teacher_password = request.POST.get('teacher-password')
        teacher_subject = request.POST.get('teacher-subject')
        platform_code = request.POST.get('platform-code')
        request.session['teacher_name'] = teacher_name
        try:
            user = User.objects.get(username=teacher_name)
            teacher_profile = TeacherProfile.objects.filter(user=user).first()
            print("A valid profile found")
            return redirect('create-room')
        except User.DoesNotExist:
            new_user = User.objects.create_user(username=teacher_name)
            new_user.set_password(teacher_password)
            new_user.save()
            platform = Platform.objects.filter(platform_code=platform_code).first()
            new_teacher_profile = TeacherProfile.objects.create(user=new_user, teacher_subject=teacher_subject, platform=platform)
            return redirect('create-room')
    return render(request, 'teachers/create_teacher_profile.html')
def create_room(request):
    teacher_name = request.session['teacher_name']
    print(teacher_name)
    if request.method == 'POST':
        room_name = request.POST.get('room-name')
        room_code = request.POST.get('room-code')
        user = User.objects.filter(username=teacher_name).first()
        teacher = TeacherProfile.objects.filter(user=user).first()
        print(teacher)
        new_room = Room.objects.create(room_name=room_name, room_code=room_code, teacher=teacher)
        return redirect('room-view', room_name=room_name, teacher_name=teacher_name)
        print("Room created!!")

    context = {'teacher_name': teacher_name}
    return render(request, 'teachers/create_room.html', context)
def logout_teacher(request):
    try:
        del request.session['teacher_name']
    except KeyError:
        pass
    return redirect('create-teacher-profile')
def room_view(request, room_name, teacher_name):
    try:
        room = Room.objects.get(room_name = room_name)
    except Room.DoesNotExist:
        return redirect('create-room')
    context = {'room_name': room_name, 'teacher_name':teacher_name}
    return render(request, 'teachers/room_view.html',context)
def manage_assignments(request, room_name, teacher_name):
    user = User.objects.filter(username=teacher_name).first()
    teacher = TeacherProfile.objects.filter(user=user).first()
    room = Room.objects.filter(room_name=room_name).first()
    print(room)
    assignments = Assignment.objects.filter(room=room)
    print(teacher)
    if request.method == 'POST':
        assignment_title = request.POST.get('assignment-title')
        assignment_file = request.FILES.get('assignment-file')
        new_assignment = Assignment.objects.create(assignment_title=assignment_title, assignment_file=assignment_file, uploaded_by=teacher, room=room)
        print("assignment created")
        return redirect('room-view', room_name=room_name, teacher_name=teacher_name)
    context = {'assignments':assignments}
    return render(request,'teachers/manage_assignments.html', context)
def delete_assignment(request, assignment_id):
    if request.method == 'POST':
        print(assignment_id)
        assignment = get_object_or_404(Assignment,id=assignment_id)
        print(assignment.assignment_title)
        assignment.delete()
        print("Deleted successfully")
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)