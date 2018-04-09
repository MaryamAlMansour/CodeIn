from rest_framework import routers
from .views import ProjectReadView, PortfolioReadView, PortfolioWriteView, ProjectWriteView, FollowersView
from django.conf.urls import url
import platforms.views

router = routers.SimpleRouter()
router.register(r'project', ProjectReadView)
router.register(r'project_write', ProjectWriteView)
router.register(r'portfolio', PortfolioReadView)
router.register(r'portfolio_write', PortfolioWriteView)
router.register(r'followers', FollowersView)
urlpatterns = router.urls
urlpatterns.append(url(r'delete_portfolio/(?P<username>\w+)/', platforms.views.delete_portfolio, name='delete-portfolio'))
urlpatterns.append(url(r'delete_project/(?P<username>\w+)/', platforms.views.delete_project, name='delete-project'))

