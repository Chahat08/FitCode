from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Problem, Comment, ProblemURL
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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
                                           'urls': urls
                                           })