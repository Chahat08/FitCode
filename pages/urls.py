# pages/urls.py

from django.urls import path
from .views import HomePageView, ProfilePageView, CodePageView, TextPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('profile/', ProfilePageView.as_view(), name='profile'),
        path('code-editor/', CodePageView, name='code'),
        path('text-editor/', TextPageView, name='text'),
    ]