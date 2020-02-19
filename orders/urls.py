from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registration", views.registration_view, name="registration"),
    path("register", views.register, name="register"),
    path("get_product_info", views.get_product_info, name="get_product_info"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
]
