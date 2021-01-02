from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from accounts.views import register_view

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    url('register/', register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name="logout"),
    path('user', views.user_detail, name='user_detail'),
    path('chat_with/<int:user_id>', views.chat_with, name='chat_with'),
    path('update_user', views.update_user, name='update_user'),
    path('update_address/<int:address_id>', views.update_address, name='update_address'),
    path('create_address', views.create_address, name='create_address'),
]