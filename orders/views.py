from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse

from .models import User


def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"messages": None})
    context = {"user": request.user}
    return render(request, "orders/index.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "orders/login.html", {"message": "Invalid credentials"})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    user = User(
        username=request.POST["username"],
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        password=request.POST["password"],
        email=request.POST["email"],
    )
    user.save()
    context = {"user": user}
    return render(request, "orders/index.html", context)


def registration_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    return render(request, "orders/registration.html")
