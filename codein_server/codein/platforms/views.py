from rest_framework import viewsets
from .models import Project, Portfolio, Contact
from .serializers import ProjectSerializerRead, PortfolioSerializerRead, PortfolioSerializerWrite, ProjectSerializerWrite, ContactSerializer


class FollowersView(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    model = Contact
    serializer_class = ContactSerializer


class PortfolioWriteView(viewsets.ModelViewSet):

    queryset = Portfolio.objects.all()
    model = Portfolio
    serializer_class = PortfolioSerializerWrite

    def perform_create(self, serializer):
        #Force author to the current user on save
        serializer.save(user=self.request.user)


class PortfolioReadView(viewsets.ModelViewSet):

    queryset = Portfolio.objects.all()
    model = Portfolio
    serializer_class = PortfolioSerializerRead


class ProjectReadView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    model = Project
    serializer_class = ProjectSerializerRead


class ProjectWriteView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    model = Project
    serializer_class = ProjectSerializerWrite

    def perform_create(self, serializer):
        #Force author to the current user on save
        serializer.save(user=self.request.user)

