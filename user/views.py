
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout

from user.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('posts')
    template_name = 'signup.html'

    # Set user Group on registration
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)
            logout(request)

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            return redirect("posts")
        else:
            return render(request, self.template_name, {'form' : form })






