from django.shortcuts import get_object_or_404, render
from django.http import Http404,HttpResponse
from django.template import loader
from django.views import generic
from django.urls import reverse

from .models import Question

# def index(request):
#     question_list = Question.objects.order_by('-pub_date')
#     context = {'question_list': question_list}
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # by default the context object is named object_list
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])

    selected_choice.votes+=1
    selected_choice.save()
    
    return HttpResponse(reverse('polls:results', args=(question.id,)))

class CreateView(generic.CreateView):
    model = Question
    fields = 'question_text',
    template_name = 'polls/create.html'
    

