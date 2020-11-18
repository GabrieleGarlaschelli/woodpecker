from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('users/login', auth_views.LoginView.as_view(), name='login'),

    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('about_us', views.about_us, name='about_us'),
    path('user', views.user_detail, name='user_detail'),

    path('<int:woodwork_id>/', views.detail, name='detail'),
    path('<int:woodwork_id>/order', views.order, name='order'),
]