from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.dateparse import parse_date
from django.urls import reverse
import datetime
from .forms import UserRegisterForm
from .models import Address, Customer, CustomUser, Message, Chat
from woodworks.models import Order
from accounts.email_backend import EmailBackend 
from .services.messages_handler import close_chat_with_user
from .services.email_handler import send

def superuser_check(user):
  return user.is_superuser

def register_view(request):
    next = request.GET.get('next')
    title = 'Registrazione'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        # new_user = authenticate(username=user.username, password=user.password)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        if next:
            return redirect(next)
        return redirect(reverse('user_detail'))
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

@permission_required('accounts.view_chat', raise_exception=True)
def chat_with(request, user_id):
  chat_with_user = CustomUser.objects.get(pk=user_id)
  chat = Chat.objects.get(user__pk=user_id)
  messages = None
  if chat != None:
    messages = Message.objects.filter(chat__pk=chat.id).order_by('created_at')
  return render(request, 'chat.html', {'chat_with_user': chat_with_user, 'messages': messages})

@login_required
def close_chat(request, chat_user_id):
  result = close_chat_with_user(chat_user_id)
  return JsonResponse({'result': True})

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

