from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from django.urls import reverse
import datetime

from .models import Address

# Create your views here.
@login_required
def user_detail(request): 
  addresses = Address.objects.filter(customer__pk=request.user.id)
  return render(request, 'user.html', {
    "addresses": addresses
  })

@login_required
def update_user(request):
  birthday = request.POST.get('birthday')

  if birthday != None and birthday != '':
    birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()
  else:
    birthday = None
  
  customer = request.user.customer
  customer.birthday = birthday
  customer.save()

  addresses = Address.objects.filter(customer__pk=request.user.id)
  return redirect(reverse('user_detail'))

@login_required
def update_address(request, address_id): 
  return redirect(reverse('user_detail'))
