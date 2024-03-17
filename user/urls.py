from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path
from user import views

urlpatterns=[
    path('signup/', views.SignUp_Customer.as_view(), name="signup_customer"),
    path('signup/', views.SignUp_Seller.as_view(), name="signup_seller"),
    path("choice/", views.choice, name="choice"),


]