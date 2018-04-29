<<<<<<< HEAD
from rest_framework import routers
from .views import ProjectReadView, PortfolioReadView, PortfolioWriteView, ProjectWriteView#, FollowersView
import platforms.views
from .views import ProjectReadView, PortfolioReadView, PortfolioWriteView, ProjectWriteView, FollowersReadView
=======
from rest_framework import routers
from .views import ProjectReadView, PortfolioReadView, PortfolioWriteView, ProjectWriteView, FollowersReadView, FollowersWriteView
>>>>>>> 63d9dc499ea31fd48fbcdcc4a7a26ab0b5601989
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

urlpatterns.append(url(r'delete_portfolio/(?P<username>\w+)/', platforms.views.delete_portfolio, name='delete-portfolio'))
urlpatterns.append(url(r'delete_project/(?P<projectname>[\w ]+)/', platforms.views.delete_project, name='delete-project'))
urlpatterns.append(url(r'unfollow/(?P<pk_to>\d+)/(?P<pk_from>\d+)/', platforms.views.unfollow, name='unfollow'))


'''
To test:

for project name: 
localhost/platform/project/get_search_proj/?search_proj_name=Python

for pulling projects of specific user:
localhost/platform/project/get_search_proj/?search_user_projs=Alla 

'''
