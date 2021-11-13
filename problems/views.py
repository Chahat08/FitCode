from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Problem, Comment, ProblemURL
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from environs import Env

env=Env()
env.read_env()

# Create your views here.
class ProblemListView(LoginRequiredMixin, ListView):
    model=Problem
    context_object_name='problem_list'
    template_name='problems/problem_list.html'
    login_url='account_login'


@login_required(login_url='account_login')
def ProblemDetailView(request, uuid):
    template_name = 'problems/problem_detail.html'
    problem = get_object_or_404(Problem, id=uuid)
    comments = problem.comments.all()

    urls=problem.urls.all()

    new_comment = None
    
    CODE_API = env('CODE_API_URL')
    TEXT_API = env('TEXT_API_URL')


    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.problem = problem
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'problem': problem, 
                                           'comments': comments,
                                          'comment_form': comment_form,
                                           'urls': urls,
                                           'code_url':CODE_API,
                                           'text_url':TEXT_API,
                                           })


class SearchResultsListView(LoginRequiredMixin, ListView):
    model=Problem
    context_object_name='problem_list'
    template_name='problems/search_results.html'
    login_url='account_login'

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Problem.objects.filter(
            Q(title__icontains=query)|
            Q(subject__icontains=query)|
            Q(topic__icontains=query)
            ) 