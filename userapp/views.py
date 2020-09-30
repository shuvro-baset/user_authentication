from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from userapp.forms import CreateUserForm
from django.contrib import messages


def home(request):
    return render("this is home page", )


def login(request):
    context = {}
    return render(request, "login.html", context)


def signup(request):
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
