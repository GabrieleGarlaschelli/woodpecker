from django.shortcuts import render
from django.http import HttpResponse

from .models import Woodwork

def index(request):
  woodworks = Woodwork.objects.order_by('created_at')
  return render(request, 'index.html', {'woodworks': woodworks})


def detail(request, woodwork_id):
    return HttpResponse("You're looking at woodwork %s." % woodwork_id)