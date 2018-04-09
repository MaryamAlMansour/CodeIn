from django.urls import path
from django.conf.urls import url
import server.views

urlpatterns = [
    url(r'deactivate_user/(?P<username>\w+)/', server.views.deactivate_user, name='deactivate-user'),
    url(r'activate_user/(?P<username>\w+)/', server.views.activate_user, name='activate-user'),
]
