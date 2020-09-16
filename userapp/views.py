from django.shortcuts import render


def home():
    return render("this is home page", )

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "registration.html")