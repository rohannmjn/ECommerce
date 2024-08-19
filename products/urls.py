
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("products_lists", views.list_products, name="list_products"),
    path("products_details/<pk>", views.detail_products, name="detail_products"),
    
]