from django.shortcuts import render
from rest_framework import viewsets
from .models import Search
from .serializers import SearchSerializer

import django_filters.rest_framework
from django.contrib.auth.models import User
from rest_framework import generics

# Create your views here.

class SearchView(viewsets.ModelViewSet):
#   serializer_class = SearchSerializer   
#   queryset = Search.objects.none()
#   model = Search
#  serializer_class = SearchSerializer
    queryset = User.objects.all()
    serializer_class = SearchSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    search_fields = ('user', 'name', 'description')
