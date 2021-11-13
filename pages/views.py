from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name='home.html'
    login_url='account_login'

class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name='profile.html'
    login_url='account_login'

class CodePageView(LoginRequiredMixin, TemplateView):
    template_name='code.html'
    login_url='account_login'

class TextPageView(LoginRequiredMixin, TemplateView):
    template_name='text.html'
    login_url='account_login'