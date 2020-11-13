from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('user', views.user_detail, name='user_detail'),
    path('<int:woodwork_id>/', views.detail, name='detail')
]