from django.urls import path, include
from django.contrib.auth import views as auth_views
from register import views as v
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name="logout"),
    path('user', views.user_detail, name='user_detail'),
    path('update_user', views.update_user, name='update_user'),
    path('update_address/<int:address_id>', views.update_address, name='update_address'),
    path('create_address', views.create_address, name='create_address'),
    path('register/',v.register, name="register"),
]