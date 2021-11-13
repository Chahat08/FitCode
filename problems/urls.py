# problems urls
from django.urls import path
from .views import ProblemListView, ProblemDetailView

urlpatterns=[
    path('', ProblemListView.as_view(), name='problem_list'),
    path('<uuid:uuid>', ProblemDetailView.as_view(), name='problem_detail'),
    ]