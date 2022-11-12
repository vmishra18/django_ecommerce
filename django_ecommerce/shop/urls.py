from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="ShopHome"),

    path("about/",views.about, name="AboutUs" ),

    path("contact/",views.contact, name="contact" ),

    path("tracker/",views.tracker, name="tracker" ),

    path("search/",views.search, name="search" ),

    path("productview/<int:myid>",views.productview, name="productview" ),
   
    path("checkout/",views.checkout, name="checkout" ),

    path("cartitem/",views.cartitem, name="cartitem" )



]
