from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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
        print(user.portfolio.image)
        user.save()
        context['msg'] = 'Profile successfully enabled.'
    except User.DoesNotExist:
        context['msg'] = 'User does not exist.'
    except Exception as e:
        context['msg'] = str(e)
    print(context['msg'])
    return Response(status=status.HTTP_200_OK)
