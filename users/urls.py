from django.urls import path, include
from . import views
from users.views import SignUpView,LoginView

urlpatterns = [
path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('account/', views.account ,name='account'),

]