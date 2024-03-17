from django.forms import ModelForm, TextInput, PasswordInput
from .models import Customer,Seller


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ("name","password")
        widgets = ({
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "name"
            }),
            "password": PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "password "
            }),


        })


class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ("company_name","password")
        widgets = ({
            "company_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "name"
            }),
            "password": PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "password "
            }),


        })