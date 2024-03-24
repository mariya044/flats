import os

from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout, get_user_model

from users.forms import CustomUserCreationForm

from users.models import CustomUser

from flat.models import Post


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage')
    template_name = 'signup.html'

    # Set user Group on registration
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # One user Group
            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)
            logout(request)
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            return redirect('posts')
        else:
            return render(request, self.template_name, {'form' : form })




class LoginView(LoginView):
    template_name = 'login.html'

    # Redirect from login page in case user already authenticated and loggedin
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('homepage')
        return self.render_to_response(self.get_context_data())



@login_required
def account(request):
    context={
        "posts":CustomUser.objects.filter(username=request.user),
        "flats":  Post.objects.filter(custom_user=request.user)
    }

    return render(request, 'account.html', context)
# Create your views here.
