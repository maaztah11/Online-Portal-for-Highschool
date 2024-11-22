from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import*

# Create your views here.
#Home Page
def index(request):
    return render(request, 'administration/index.html')
#View that handles creation of a new admin and in case an old one exists it fetches its record
def register_admin(request):
    if request.method == 'POST':
        username = request.POST.get('admin-name')
        password = request.POST.get('admin-pass')
        try:
            user = User.objects.get(username=username)
            request.session['admin_name'] = username
            admin = Organization_Admin.objects.filter(user=user).first()
            platform = Platform.objects.filter(admin=admin).first()
            platform_name = platform.platform_name
            if platform:
                return redirect('admin-dashboard', platform_name)
            else:
                return redirect('add-organization', username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username)
            user.set_password(password)
            request.session['admin_name'] = username
            request.session.set_expiry(30*60)
            print(request.session['admin_name'])
            user.save()
            admin = Organization_Admin.objects.create(user=user, role='admin')
            print(f"Admin created.")
        return redirect('add-organization', username=username)
    return render(request, 'administration/register_admin.html')
#Allowing the admin to create an organization
def add_organization(request, username):
    context = {'username': username}
    if request.method == 'POST':
        platform_name = request.POST.get('platform-name')
        platform_code = request.POST.get('platform-code')
        user = User.objects.filter(username=username).first()
        print(user)
        admin = Organization_Admin.objects.filter(user=user).first()
        print(admin)
        new_platform = Platform.objects.create(platform_name=platform_name, platform_code=platform_code, admin=admin)
        print("Platform created.")
        return redirect('admin-dashboard', platform_name=platform_name)
    return render(request, 'administration/add_organization.html', context)
#Dashboard for admin
def admin_dashboard(request, platform_name):
    admin_name = request.session['admin_name']
    if not admin_name:
        return redirect('register-admin')
    context = {'platform_name': platform_name}
    return render(request, 'administration/admin_dashboard.html',context)
#Logout admin based on session
def admin_logout(request):
    try:
        del request.session['admin_name']
    except KeyError:
        pass
    return redirect('register-admin')