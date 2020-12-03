from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from django.urls import reverse
import datetime
from .forms import UserRegisterForm
from .models import Address, Customer
from woodworks.models import Order
from  accounts.email_backend import EmailBackend 

def register_view(request):
    next = request.GET.get('next')
    title = 'Registrazione'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=user.password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'registration/register.html', {'form': form, 'title': title})

def logout_view(request):
  logout(request)
  return redirect(reverse('login') + "?next=" + reverse('user_detail'))

@login_required
def user_detail(request): 
  # TODO create customer on registration
  if Customer.objects.filter(user_id=request.user.id).count() == 0:
    customer = Customer.objects.create(user_id=request.user.id)
    customer.save()

  addresses = Address.objects.filter(customer__pk=request.user.customer.id)
  orders = Order.objects.filter(customer__pk=request.user.customer.id)
  return render(request, 'user.html', {
    "addresses": addresses,
    "orders": orders
  })

@login_required
def update_user(request):
  birthday = request.POST.get('birthday')

  if birthday != None and birthday != '':
    birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()
  else:
    birthday = None
  
  if Customer.objects.filter(user_id=request.user.id).count() == 0:
    customer = Customer.objects.create(user_id=request.user.id)
    customer.save()

  customer = request.user.customer
  customer.birthday = birthday
  customer.save()

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
  # TODO create customer on registration
  if Customer.objects.filter(user_id=request.user.id).count() == 0:
    customer = Customer.objects.create(user_id=request.user.id)
    customer.save()
    
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

