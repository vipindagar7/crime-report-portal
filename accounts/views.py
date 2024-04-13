from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from .models import Custom_user ,  Profile
import uuid
from .email import send_verification_email

# Create your views here.

def newuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        auth_token = str(uuid.uuid4())
        is_inspector = False
        if Custom_user.objects.filter(email = email).exists():
            messages.error(request , 'Email already exists')
            return redirect('/accounts/newuser/')
        else:
            user = Custom_user.objects.create_user(email = email , first_name = first_name , last_name = last_name , is_inspector = is_inspector , auth_token = auth_token)
            send_verification_email(email , auth_token)
            user.set_password(password)
            user.save()
            return redirect('/accounts/login/')
    return render(request , 'accounts/newuser.html')


def verify(request , auth_token):
    try:
        user = Custom_user.objects.get(auth_token = auth_token)
        if user.is_verified:
            messages.success(request , 'Your account is already verified')
            return redirect('/accounts/login/')
        user.is_verified = True
        user.save()
        messages.success(request , 'Your account has been verified')
        return redirect('/accounts/login/')
    except Exception as e:
        messages.error(request , 'Invalid request')
        return redirect('/accounts/login/')
    

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request , email = email, password = password)
        if user is not None:
            if user.is_verified:
                login(request , user)
                return redirect('/accounts/dashboard/')
            else:
                messages.error(request , 'Please verify your email')
                return redirect('/accounts/login')
        else:
            messages.error(request , 'Invalid email or password')        
    return render(request , 'accounts/login.html')



def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')

def dashboard(request):
    user = Custom_user.objects.get(email = request.user.email)
    profile = Profile.objects.get(user = user)
    context = {'profile':profile}
    if request.method == 'POST':
        profile.user.first_name = request.POST.get('first_name')
        profile.user.last_name = request.POST.get('last_name')
        profile.user.save()
        profile.dob = request.POST.get('dob')
        profile.phone = request.POST.get('phone')
        profile.gender = request.POST.get('gender')
        profile.address = request.POST.get('address')
        profile.emergency_contact = request.POST.get('emergency_contact')
        profile.save()
        messages.success(request , 'Profile updated successfully')
        return redirect('/accounts/dashboard/')
    return render(request , 'accounts/profile.html' , context)

def manage_user(request):
    users = Custom_user.objects.all()
    context = {'users':users}
    return render(request , 'accounts/manage_user.html' , context)

def create_inspector(request):
    user = Custom_user.objects.get(email = request.user.email)
    if user.is_superuser:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            auth_token = str(uuid.uuid4())
            is_inspector = True
            is_verified = True
            inspector_id = request.POST.get('inspector_id')
            inspector_dept = request.POST.get('inspector_dept')
            inspector_desig = request.POST.get('inspector_desig')
            if Custom_user.objects.filter(email = email).exists():
                messages.error(request , 'Email already exists')
                return redirect('/accounts/create_inspector/')
            else:
                user = Custom_user.objects.create_user(email = email , first_name = first_name , last_name = last_name , is_inspector = is_inspector , auth_token = auth_token , inspector_id = inspector_id , inspector_dept = inspector_dept , inspector_desig = inspector_desig , is_verified = is_verified)

                user.set_password(password)
                user.save()
                return redirect('/accounts/manage_users/')
        return render(request , 'accounts/create_inspector.html')
    else:
        return HttpResponse('You are not authorized to view this page')
    
    
    
def view_user(request , id):
    if request.user.is_superuser:
        user = Custom_user.objects.get(id = id)
        profile = Profile.objects.get(user = user)
        context = {'profile':profile}
        return render(request , 'accounts/view_user.html' , context)
    else:
        return HttpResponse('You are not authorized to view this page')
     
    
def delete_user(request , id):
    if request.user.is_superuser:
        user = Custom_user.objects.get(id = id)
        user.delete()
        messages.success(request , 'User deleted successfully')
        return redirect('/accounts/manage_users/')
    else:
        return HttpResponse('You are not authorized to view this page')
    
def update_user(request , id):
    if request.user.is_superuser:
        user = Custom_user.objects.get(id = id)
        profile = Profile.objects.get(user = user)
        context = {'profile':profile}
        if request.method == 'POST':
            profile.user.first_name = request.POST.get('first_name')
            profile.user.last_name = request.POST.get('last_name')
            profile.user.email = request.POST.get('email')
            profile.user.save()
            profile.dob = request.POST.get('dob')
            profile.gender = request.POST.get('gender')
            profile.phone = request.POST.get('phone')
            profile.address = request.POST.get('address')
            profile.emergency_contact = request.POST.get('emergency_contact')
            profile.save()
            messages.success(request , 'Profile updated successfully')
            return redirect('/accounts/manage_users/')
        else:
            return HttpResponse("You are not authorized to view this page")
    else:
        return HttpResponse('You are not authorized to view this page')
    