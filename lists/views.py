from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import TaskList
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskListForm

# Create your views here.

class TaskListView(CreateView):
    model = TaskList
    form_class = TaskListForm
    template_name = 'tasklist.html'
    # success_url = reverse_lazy('tasklist')