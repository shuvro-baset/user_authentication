from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from userapp.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import datetime, time

from userapp.models import Session_time


@login_required(login_url='userapp:login')
def home(request):
    if request.user.is_authenticated:
        all_users = get_user_model().objects.all()
        ses = request.user

        context = {'allusers': all_users, 'ses': ses}
    return render(request, 'home.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('userapp:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print("user: ",user.id)
            user_id = user.id
            print("user_id: ", user_id)
            login_time = time.time()

            user_session = Session_time(user= user, login_time= login_time, logout_time=None)
            user_session.save()
            print(user_session)
            if user is not None:
                login(request, user)
                return redirect('userapp:home')
            else:
                messages.info(request, 'Username or Password incorrect')
                return render(request, "login.html", )
        context = {}
        return render(request, "login.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('userapp:home')
    else:

        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account successfully create for ' + user)
                return redirect('userapp:login')
        context = {'form': form}
        return render(request, "registration.html", context)


def logoutUser(request):
    user = request.user
    # print("user: ", user.id)
    # user_ins = User.objects.get(id=user.id)
    # print(" dsdf : ", user_ins)
    logout_time = time.time()

    # session_ins = Session_time.objects.get(user=user)
    session_ins = Session_time.objects.filter(user_id=user).last()
    session_ins.logout_time = logout_time
    session_time = float(session_ins.logout_time) - float(session_ins.login_time)

    session_ins.ses_time = float(session_time)

    session_ins.save()

    print("session_time: ", session_time)

    logout(request)

    return redirect('userapp:session_time')




def changePass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateUserForm(user=request.user, data=request.POST)

            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            user = authenticate(request,  password=new_password)
            user.save()

            messages.info(request, 'password successfully changed')
            return redirect('/home/')
    else:
        return redirect('userapp:login')
    form = CreateUserForm()
    context = {'form': form}
    return render(request, "change_password.html", context)

def sessionTime(request):
    session_ins = Session_time.objects.all()
    print(session_ins)
    context = {'session_ins': session_ins}
    return render(request, "session_time.html", context)