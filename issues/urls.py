from django.urls import path
from .views import IssueListCreateView, IssueUpdateView

urlpatterns = [
    path('issues/',           IssueListCreateView.as_view()),
    path('issues/<int:pk>/',  IssueUpdateView.as_view()),
]
