from rest_framework import viewsets
from .models import Project, Portfolio, Contact
from .serializers import ProjectSerializerRead, PortfolioSerializerRead, PortfolioSerializerWrite, ProjectSerializerWrite, ContactSerializerRead
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model


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
            if isinstance(search_user_projs, int):
                queryset = queryset.filter(user=search_user_projs)
            else:
                queryset = []

        serializer = ProjectSerializerRead(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


class ProjectWriteView(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    model = Project
    serializer_class = ProjectSerializerWrite

    def perform_create(self, serializer):
        #Force author to the current user on save
        serializer.save(user=self.request.user)


@api_view(['GET',])
def delete_portfolio(request, username):
    context = {}

    try:
        User = get_user_model()
        user = User.objects.get(username=username)
        user.portfolio.delete()
        context['msg'] = 'Portfolio successfully deleted.'
    except User.DoesNotExist:
        context['msg'] = 'User does not exist.'
    except Exception as e:
        context['msg'] = str(e)
    print(context['msg'])
    return Response(status=status.HTTP_200_OK)

@api_view(['GET',])
def delete_project(request, projectname):
    context = {}
    try:
        projects = Project.objects.all()
        print(projects)
        if projectname:
            projects = projects.filter(name=projectname)
            projects.delete()
            print(projects)
            context['msg'] = "Successfully deleted."
        else:
            context['msg'] = "Please provide a project name."
    except Exception as e:
        context['msg'] = str(e)
    print(context['msg'])
    return Response(status=status.HTTP_200_OK)

@api_view(['GET',])
def unfollow(request, pk_to, pk_from):
    context = {}
    try:
        contacts = Contact.objects.all()
        if pk_to and pk_from:
            contacts = contacts.filter(user_to=pk_to,user_from=pk_from)
            print(contacts)
            contacts.delete()
            print(contacts)
            context['msg'] = "Successfully unfollowed."
        else:
            context['msg'] = "Please provide a pk_to and pk_from."
    except Exception as e:
        context['msg'] = str(e)
    print(context['msg'])
    return Response(status=status.HTTP_200_OK)

