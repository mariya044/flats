from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all())


    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ('username', 'fio', "email",'gender', 'birth_date', 'groups')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ('username', 'fio', 'gender', 'birth_date', 'groups')