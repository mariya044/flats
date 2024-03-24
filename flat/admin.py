from django.contrib import admin
from flat.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","text"]



admin.site.register(Post, PostModelAdmin)


# Register your models here.


# Register your models here.

