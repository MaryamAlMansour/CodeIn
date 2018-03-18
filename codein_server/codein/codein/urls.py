from rest_framework import routers
from .views import ProjectView
from django.conf.urls import url

router = routers.SimpleRouter()
router.register(r'project', ProjectView)

urlpatterns = [

    url(r'^myportfolio/',ProjectView.as_view())

]