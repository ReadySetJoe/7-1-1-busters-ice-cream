from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import IceCream

def index(request, menu_filter=''):
  if menu_filter == 'home':
    freshest_list = IceCream.objects.all()
  elif menu_filter == 'featured':
    freshest_list = IceCream.objects.filter(featured=True)
  else:
    freshest_list = IceCream.objects.filter(available=menu_filter)

  freshest_list = freshest_list.order_by('-date_churned')
  template = loader.get_template('menu/index.html')
  context = {
      'freshest_list': freshest_list,
  }
  return HttpResponse(template.render(context, request))

def detail(request, icecream_id):
    ic = get_object_or_404(IceCream, pk=icecream_id)
    return HttpResponse("You're looking at %s." % ic.flavor)

def upvote(request, icecream_id, menu_filter='home'):
    ic = get_object_or_404(IceCream, pk=icecream_id)
    ic.score += 1
    ic.save()
    return HttpResponseRedirect(reverse('menu:index', args=(menu_filter,)))

def downvote(request, icecream_id, menu_filter='home'):
    ic = get_object_or_404(IceCream, pk=icecream_id)
    ic.score -= 1
    ic.save()
    return HttpResponseRedirect(reverse('menu:index', args=(menu_filter,)))
