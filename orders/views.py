from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.core import serializers

from .models import User, Category, Price, Product, Topping


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
        request.session["order"] = []
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
    number_of_toppings = Product.objects.get(pk=product_id).number_of_toppings
    data = serializers.serialize("json", prices)
    data_2 = serializers.serialize("json", toppings)

    return JsonResponse(
        {"prices": data, "number_of_toppings": number_of_toppings, "toppings": data_2}
    )


def add_to_cart(request):
    """add product to order in session"""
    # get added to cart item
    product_id = request.POST["product"]
    price_id = request.POST["price"]
    toppings = request.POST.getlist("topping[]")
    order = (product_id, price_id, toppings)

    # store this item in session object
    request.session["order"].append(order)
    request.session.modified = True

    return HttpResponse(200)


def cart(request):
    """get all orders from session and render it in cart"""
    orders = []
    for order in request.session["order"]:
        print(order)
        orders.append(
            {
                "product": Product.objects.get(pk=order[0]),
                "price": Price.objects.get(pk=order[1]),
                "toppings": [
                    Topping.objects.get(pk=topping_id) for topping_id in order[2]
                ],
            }
        )
    context = {"orders": orders}
    return render(request, "orders/cart.html", context)
