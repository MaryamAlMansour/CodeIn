from rest_framework import viewsets
from .models import Project, Portfolio, Contact
from .serializers import ProjectSerializerRead, PortfolioSerializerRead, PortfolioSerializerWrite, ProjectSerializerWrite, ContactSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

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

@api_view(['GET',])
def delete_project(request, username):
    context = {}

    try:
        User = get_user_model()
        user = User.objects.get(username=username)
        print(user.project)
    except User.DoesNotExist:
        context['msg'] = 'User does not exist.'
    except Exception as e:
        context['msg'] = str(e)
    print(context['msg'])
    return Response(status=status.HTTP_200_OK)
