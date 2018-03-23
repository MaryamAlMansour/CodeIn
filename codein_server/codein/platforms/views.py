from rest_framework import viewsets
from .models import Project, Portfolio
from .serializers import ProjectSerializer, PortfolioSerializer


class ProjectView(viewsets.ModelViewSet):

    queryset = Project.objects.none()
    model = Project
    serializer_class = ProjectSerializer

class PortfoliotView(viewsets.ModelViewSet):

    queryset = Portfolio.objects.none()
    model = Portfolio
    serializer_class = PortfolioSerializer
    
    def get_queryset(self):

        return self.model.objects.all()

"""
    def perform_create(self, serializer):
        #Force author to the current user on save
        serializer.save(author=self.request.user)
"""
