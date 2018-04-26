from rest_framework import routers
from .views import ProjectReadView, PortfolioReadView, PortfolioWriteView, ProjectWriteView, FollowersReadView, FollowersWriteView
from django.conf.urls import url


router = routers.SimpleRouter()
router.register(r'project/', ProjectReadView)
router.register(r'project/get_search_proj/(?P<search_proj_name>\w+)/', ProjectReadView)
router.register(r'project/get_search_proj/(?P<search_user_projs>\w+)/',ProjectReadView)
router.register(r'project_write/', ProjectWriteView)
router.register(r'portfolio/', PortfolioReadView)
router.register(r'portfolio_write/', PortfolioWriteView)
router.register(r'followers/', FollowersReadView)
router.register(r'followers_write/', FollowersWriteView)

urlpatterns = router.urls

'''
To test:

for project name: 
localhost/platform/project/get_search_proj/?search_proj_name=Python

for pulling projects of specific user:
localhost/platform/project/get_search_proj/?search_user_projs=Alla 

'''
