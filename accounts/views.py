from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

def landing(request):
    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register_lawyer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password==password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken!')
                return redirect('register_lawyer')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is laready in use!')
                    return redirect('register_lawyer')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    group = Group.objects.get(name='Advocates')
                    user.groups.add(group)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords donot match')
            return redirect('register_lawyer')

    else:
        return render(request,'accounts/adv_signup.html')

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login/')
def dashboard(request):
    is_advocate = request.user.groups.filter(name='Advocates').exists()
    is_judge = request.user.groups.filter(name='Judges').exists()
    is_officer = request.user.groups.filter(name='Officers').exists()
    
    print('advocate: ' + str(is_advocate))
    print('judge: ' + str(is_judge))
    print('officer: ' + str(is_officer))
    
    context = {
        'is_advocate': is_advocate,
        'is_judge': is_judge,
        'is_officer': is_officer,
    }
    
    if is_advocate:
        return redirect('lawyer_dashboard')
    else:
        if is_judge:
            return redirect('judge_dashboard')
        else:
            if is_officer:
                return redirect('office_dashboard')
            else:
                return render(request, 'accounts/dashboard.html', context)
                