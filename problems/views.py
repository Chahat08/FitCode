from django.shortcuts import render
from django.views.generic import ListView
from .models import Problem
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProblemListView(LoginRequiredMixin, ListView):
    model=Problem
    context_object_name='problem_list'
    template_name='problems/problem_list.html'
    login_url='account_login'