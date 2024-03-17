from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from user.forms import CustomerForm,SellerForm


class SignUp_Customer(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup_customer.html"
    success_url = reverse_lazy("login")

class SignUp_Seller(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup_seller.html"
    success_url = reverse_lazy("login")


def choice(request):
    return  render(request, "choice.html")


