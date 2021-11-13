from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from environs import Env

env=Env()
env.read_env()

# Create your views here.
class HomePageView(TemplateView):
    template_name='home.html'
    # login_url='account_login'

class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name='profile.html'
    login_url='account_login'

class AboutPageView(LoginRequiredMixin, TemplateView):
    template_name='about.html'
    login_url='account_login'

@login_required(login_url='account_login')
def CodePageView(request):
    CODE_API = env('CODE_API_URL')
    template_name='code.html'

    return render(request, template_name, {'code_url':CODE_API})

@login_required(login_url='account_login')
def TextPageView(request):
    TEXT_API = env('TEXT_API_URL')
    template_name='text.html'

    return render(request, template_name, {'text_url':TEXT_API})
