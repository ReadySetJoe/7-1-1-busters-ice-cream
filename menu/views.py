from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import IceCream

def index(request):
    freshest_list = IceCream.objects.order_by('-date_churned')
    template = loader.get_template('menu/index.html')
    context = {
        'freshest_list': freshest_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, icecream_id):
    return HttpResponse("You're looking at %s." % icecream_id)

def featured(request):
    freshest_list = IceCream.objects.get(featured=True).order_by('-date_churned')
    template = loader.get_template('menu/index.html')
    context = {
        'freshest_list': freshest_list,
    }
    return HttpResponse(template.render(context, request))


def daily(request):
    freshest_list = IceCream.objects.order_by('-date_churned')[:5]
    template = loader.get_template('menu/index.html')
    context = {
        'freshest_list': freshest_list,
    }
    return HttpResponse(template.render(context, request))

def weekly(request):
    freshest_list = IceCream.objects.order_by('-date_churned')[:5]
    template = loader.get_template('menu/index.html')
    context = {
        'freshest_list': freshest_list,
    }
    return HttpResponse(template.render(context, request))

def seasonal(request):
    freshest_list = IceCream.objects.order_by('-date_churned')[:5]
    template = loader.get_template('menu/index.html')
    context = {
        'freshest_list': freshest_list,
    }
    return HttpResponse(template.render(context, request))