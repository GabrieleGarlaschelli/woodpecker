from django.shortcuts import render
from django.http import HttpResponse

from .models import Woodwork

def index(request):
  woodworks = Woodwork.objects.order_by('created_at')
  return render(request, 'index.html', {'woodworks': woodworks})


def detail(request, woodwork_id):
  woodwork = Woodwork.objects.get(pk=woodwork_id)
  return render(request, 'woodworks/detail.html', {
    'woodwork': woodwork
  })

def list(request):
  woodworks = Woodwork.objects.order_by('created_at')
  return render(request, 'woodworks/list.html', {
    'woodworks': woodworks
  })

def about_us(request): 
  return render(request, 'about_us.html')

def user_detail(request): 
  return render(request, 'user.html')