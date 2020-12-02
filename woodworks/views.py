from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import datetime

from .models import Woodwork, Like

from woodworks.services.order import order_woodwork

def index(request):
  woodworks = Woodwork.objects.order_by('-publication_date')[:3]
  return render(request, 'index.html', {'woodworks': woodworks})


def detail(request, woodwork_id):
  woodwork = Woodwork.objects.get(pk=woodwork_id)
  return render(request, 'woodworks/detail.html', {
    'woodwork': woodwork
  })

@login_required
def order(request, woodwork_id):
  notes = request.POST.get('notes')
  quantity = request.POST.get('quantity')
  expiration_date = request.POST.get('expiration_date')
  success = order_woodwork(woodwork_id, request.user.customer.id, notes, quantity, expiration_date)
  return render(request, 'woodworks/order_successful.html')

@login_required
def is_liked(request, woodwork_id):
  woodwork = Woodwork.objects.get(pk=woodwork_id)
  return JsonResponse({'result': woodwork.is_liked(request.user)})

@login_required
def like(request, woodwork_id):
  like = Like.objects.create(user=request.user, woodwork_id=woodwork_id, added_at=datetime.datetime.now())
  like.save()
  return JsonResponse({'result': True})

@login_required
def unlike(request, woodwork_id):
  Like.objects.filter(user=request.user, woodwork_id=woodwork_id).delete()
  return JsonResponse({'result': True})


def list(request):
  woodworks = Woodwork.objects.order_by('created_at')
  return render(request, 'woodworks/list.html', {
    'woodworks': woodworks
  })

def about_us(request): 
  return render(request, 'about_us.html')