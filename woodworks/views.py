from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Q
import datetime

from .models import Woodwork, Like, Rating
from accounts.models import Chat, Message

from woodworks.services.order import order_woodwork
from woodworks.services.rate import rate_woodwork

def index(request):
  woodworks = Woodwork.objects.order_by('-publication_date')[:3]
  return render(request, 'index.html', {'woodworks': woodworks})

def detail(request, woodwork_id):
  woodwork = Woodwork.objects.get(pk=woodwork_id)
  ratings = Rating.objects.filter(woodwork__pk=woodwork_id)

  average_rating = Rating.objects.filter(woodwork__pk=woodwork_id).aggregate(average_rating=Avg('rate'))
  if average_rating['average_rating'] == None:
    average_rating['average_rating'] = 0
  return render(request, 'woodworks/detail.html', {
    'woodwork': woodwork,
    'ratings': ratings,
    'avarage_rating': average_rating['average_rating']
  })

def rate(request, woodwork_id):
  rate = request.POST.get('rate')
  comment = request.POST.get('comment')
  success = rate_woodwork(woodwork_id, request.user.customer.id, rate, comment)
  return JsonResponse({'success': success})

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

  messages = None
  if request.user != None:
    chat = Chat.objects.filter(user__pk=request.user.id, status=Chat.OPENED).first()
    messages = None
    if chat != None:
      messages = Message.objects.filter(chat__pk=chat.id).order_by('created_at')

  return render(request, 'woodworks/list.html', {
    'woodworks': woodworks,
    'messages': messages
  })

def about_us(request): 
  return render(request, 'about_us.html')
  
def searchbar(request):
  query = request.GET['query']
  allWoodworks = Woodwork.objects.filter(title__icontains=query)
  params = {'allWoodworks': allWoodworks}
  return render(request, 'searchbar.html', params)


