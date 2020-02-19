from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.core import serializers

from .models import User, Category, Price, Product


def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"messages": None})
    context = {"user": request.user, "menu": Category.objects.all()}
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


def get_product_info(request):
    product_id = request.GET["productId"]
    prices = Price.objects.filter(product=product_id)
    toppings = Product.objects.get(pk=product_id).toppings.all()
    data = serializers.serialize("json", prices)
    data_2 = serializers.serialize("json", toppings)

    return JsonResponse({"prices": data, "toppings": data_2})


def add_to_cart(request):
    product_id = request.POST["product"]
    price_id = request.POST["price"]
    topping = request.POST["topping"]
    print(product_id, price_id, topping)
    return HttpResponse(200)
