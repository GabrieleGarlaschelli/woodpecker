from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.dateparse import parse_date
from django.urls import reverse
import datetime

from .models import Address

def logout_view(request):
  logout(request)
  return redirect(reverse('login') + "?next=" + reverse('user_detail'))

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
  address = Address.objects.get(pk=address_id)

  address.address = request.POST.get('address')
  address.county = request.POST.get('county')
  address.postal_code = request.POST.get('postal_code')
  address.city = request.POST.get('city')
  address.firstname = request.POST.get('firstname')
  address.lastname = request.POST.get('lastname')
  address.save()

  return redirect(reverse('user_detail'))

@login_required
def create_address(request):
  address = Address()
  address.customer = request.user.customer
  address.address = request.POST.get('address')
  address.county = request.POST.get('county')
  address.postal_code = request.POST.get('postal_code')
  address.city = request.POST.get('city')
  address.firstname = request.POST.get('firstname')
  address.lastname = request.POST.get('lastname')
  address.save()

  return redirect(reverse('user_detail'))

