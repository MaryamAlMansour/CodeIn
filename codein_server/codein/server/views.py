from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import UserDetailsSerializer
from .models import User
from rest_framework.decorators import list_route


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

    @list_route(methods=['get'])
    def get_search_user(self, request):
        queryset = User.objects.all()

        search_user_name = None
        search_email = None

        if 'search_user_name' in self.request.query_params:
            search_user_name = self.request.query_params['search_user_name']
        if search_user_name:
            queryset = queryset.filter(username=search_user_name)

        if 'search_email' in self.request.query_params:
            search_email = self.request.query_params['search_email']
        if search_email:
            queryset = queryset.filter(email=search_email)

        serializer = UserDetailsSerializer(queryset, many=True, context=self.get_serializer_context())
        return Response(serializer.data)


# Create your views here.
@api_view(['GET',])
def deactivate_user(request, username):
    context = {}

    try:
        User = get_user_model()
        print(User)
        print(username)
        user = User.objects.get(username=username)
        print ('2')
        user.is_active = False
        user.save()
        context['msg'] = 'Profile successfully disabled.'
    except User.DoesNotExist:
        context['msg'] = 'User does not exist.'
    except Exception as e:
        context['msg'] = str(e)
    print (context['msg'])
    return Response(status=status.HTTP_200_OK)

@api_view(['GET',])
def activate_user(request, username):
    context = {}

    try:
        User = get_user_model()
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        context['msg'] = 'Profile successfully enabled.'
    except User.DoesNotExist:
        context['msg'] = 'User does not exist.'
    except Exception as e:
        context['msg'] = str(e)
    print(context['msg'])
    return Response(status=status.HTTP_200_OK)
