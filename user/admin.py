from django.contrib import admin
from user.models import Customer,Seller

class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["name","password"]

admin.site.register(Customer, CustomerModelAdmin)


class SellerModelAdmin(admin.ModelAdmin):
    list_display = ["company_name","password"]

admin.site.register(Seller, SellerModelAdmin)

# Register your models here.
