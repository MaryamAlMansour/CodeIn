from rest_framework import routers
from .views import ProjectView, PortfoliotView
from django.conf.urls import url

router = routers.SimpleRouter()
router.register(r'project', ProjectView)
router.register(r'portfolio', PortfoliotView)

urlpatterns = router.urls

    
#    [

 #   url(r'^project/',ProjectView)

#]
 #   """
