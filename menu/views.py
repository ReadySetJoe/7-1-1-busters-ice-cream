from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test

from .models import IceCream

def home(request, menu_filter=''):
  if menu_filter == 'home':
    freshest_list = IceCream.objects.all()
  elif menu_filter == 'featured':
    freshest_list = IceCream.objects.filter(featured=True)
  else:
    freshest_list = IceCream.objects.filter(available=menu_filter)

  freshest_list = freshest_list.order_by('-date_churned')
  template = loader.get_template('menu/home.html')
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
    return HttpResponseRedirect(reverse('menu:home', args=(menu_filter,)))

def downvote(request, icecream_id, menu_filter='home'):
    ic = get_object_or_404(IceCream, pk=icecream_id)
    ic.score -= 1
    ic.save()
    return HttpResponseRedirect(reverse('menu:home', args=(menu_filter,)))

class CreateView(UserPassesTestMixin, generic.CreateView):
    model = IceCream
    fields = 'flavor','featured','base','available',
    template_name = 'menu/create.html'

    def test_func(self):
      return self.request.user.is_superuser

    def handle_no_permission(self):
      return redirect('menu:index')
    
class IndexView(generic.ListView):
    template_name = 'menu/index.html'
    def get_queryset(self):
        return IceCream.objects.all()

class DeleteView(generic.DeleteView):
    template_name = 'menu/delete.html'
    model = IceCream
    success_url = reverse_lazy('menu:home',args=('home',))

def is_superuser_check(user):
  return user.is_superuser
