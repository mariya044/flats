from user.views import SignUpView

from django.urls import path
from user import views

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]