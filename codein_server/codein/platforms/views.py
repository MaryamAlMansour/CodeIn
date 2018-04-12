from rest_framework import viewsets
from .models import Project, Portfolio, Contact
from .serializers import ProjectSerializerRead, PortfolioSerializerRead, PortfolioSerializerWrite, ProjectSerializerWrite, ContactSerializerRead
from url_filter.integrations.drf import DjangoFilterBackend


class FollowersReadView(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    model = Contact
    serializer_class = ContactSerializerRead


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
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user']


class ProjectReadView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    model = Project
    serializer_class = ProjectSerializerRead
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user','name']



'''
    def get_queryset(self):
        # allow rest api to filter by submissions 
        queryset = Project.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)

        return queryset
'''


class ProjectWriteView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    model = Project
    serializer_class = ProjectSerializerWrite

    def perform_create(self, serializer):
        #Force author to the current user on save
        serializer.save(user=self.request.user)

