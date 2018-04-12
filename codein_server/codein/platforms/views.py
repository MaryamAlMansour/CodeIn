from rest_framework import viewsets
from .models import Project, Portfolio, Contact
from .serializers import ProjectSerializerRead, PortfolioSerializerRead, PortfolioSerializerWrite, ProjectSerializerWrite, ContactSerializerRead
from rest_framework.decorators import list_route
from rest_framework.response import Response


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


class ProjectReadView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializerRead

    @list_route(methods=['get'])
    def get_search_proj(self, request):
        queryset = Project.objects.all()

        search_proj_name = None
        search_user_projs = None

        if 'search_proj_name' in self.request.query_params:
            search_proj_name = self.request.query_params['search_proj_name']
        if search_proj_name:
            queryset = queryset.filter(name=search_proj_name)

        if 'search_user_projs' in self.request.query_params:
            search_user_projs = self.request.query_params['search_user_projs']
        if search_user_projs:
            queryset = queryset.filter(user=search_user_projs)

        serializer = ProjectSerializerRead(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


class ProjectWriteView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    model = Project
    serializer_class = ProjectSerializerWrite

    def perform_create(self, serializer):
        #Force author to the current user on save
        serializer.save(user=self.request.user)

