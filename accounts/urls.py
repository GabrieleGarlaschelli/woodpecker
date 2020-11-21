from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('user', views.user_detail, name='user_detail'),
    path('update_user', views.update_user, name='update_user'),
    path('update_address/<int:address_id>', views.update_address, name='update_address'),
]