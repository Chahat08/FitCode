from django.urls import path
from .views import TaskListView

urlpatterns=[
    path('tasklist/', TaskListView.as_view(), name='tasklist'),

    ]