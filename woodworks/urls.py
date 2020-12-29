from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('about_us', views.about_us, name='about_us'),
    path('searchbar', views.searchbar, name='searchbar'),

    path('<int:woodwork_id>/', views.detail, name='woodwork_detail'),
    path('<int:woodwork_id>/order', views.order, name='order'),
    path('<int:woodwork_id>/is_liked', views.is_liked, name='is_liked'),
    path('<int:woodwork_id>/like', views.like, name='like'),
    path('<int:woodwork_id>/unlike', views.unlike, name='unlike'),
    path('<int:woodwork_id>/rate', views.rate, name='rate'),
]