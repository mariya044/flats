from django.contrib import admin
from django.contrib import admin
from users.models import CustomUser

class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ["fio","gender"]

admin.site.register(CustomUser, CustomUserModelAdmin)

