from rest_framework import routers
from .views import ProjectView
from django.conf.urls import url

router = routers.SimpleRouter()
router.register(r'project', ProjectView)

urlpatterns = router.urls

    
#    [

 #   url(r'^project/',ProjectView)

#]
 #   """