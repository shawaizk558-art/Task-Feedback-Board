from rest_framework import generics
from .models import Issue
from .serializers import IssueSerializer

class IssueListCreateView(generics.ListCreateAPIView):
    queryset         = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueUpdateView(generics.UpdateAPIView):
    queryset          = Issue.objects.all()
    serializer_class  = IssueSerializer
    http_method_names = ['patch']
