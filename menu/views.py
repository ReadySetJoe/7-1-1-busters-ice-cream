from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import IceCream

def index(request):
    freshest_list = IceCream.objects.order_by('-date_churned')
    return theRest(request, freshest_list)
    

def theRest(request, freshest_list):
  template = loader.get_template('menu/index.html')
  context = {
      'freshest_list': freshest_list,
  }
  return HttpResponse(template.render(context, request))


def detail(request, icecream_id):
    return HttpResponse("You're looking at %s." % icecream_id)

def featured(request):
    freshest_list = IceCream.objects.filter(featured=True).order_by('-date_churned')
    return theRest(request, freshest_list)

def daily(request):
    freshest_list = IceCream.objects.filter(available='daily').order_by('-date_churned')
    return theRest(request, freshest_list)

def weekly(request):
    freshest_list = IceCream.objects.filter(available='weekly').order_by('-date_churned')
    return theRest(request, freshest_list)

def seasonal(request):
    freshest_list = IceCream.objects.filter(available='seasonal').order_by('-date_churned')
    return theRest(request, freshest_list)

