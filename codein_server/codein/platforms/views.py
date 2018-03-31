from rest_framework import viewsets
from .models import Project, Portfolio
from .serializers import ProjectSerializerRead, PortfolioSerializer, ProjectSerializerWrite


class ProjectReadView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    model = Project
    serializer_class = ProjectSerializerRead


class PortfolioView(viewsets.ModelViewSet):

    queryset = Portfolio.objects.all()
    model = Portfolio
    serializer_class = PortfolioSerializer


class ProjectWriteView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    model = Project
    serializer_class = ProjectSerializerWrite

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

"""
    def perform_create(self, serializer):
        #Force author to the current user on save
        serializer.save(author=self.request.user)
"""
