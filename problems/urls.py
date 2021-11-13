# problems urls
from django.urls import path
from .views import ProblemListView, ProblemDetailView, SearchResultsListView

urlpatterns=[
    path('', ProblemListView.as_view(), name='problem_list'),
    path('<uuid:uuid>', ProblemDetailView, name='problem_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),

    ]