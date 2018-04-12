from rest_framework import routers
from .views import ProjectReadView, PortfolioReadView, PortfolioWriteView, ProjectWriteView, FollowersReadView
from django.conf.urls import url


router = routers.SimpleRouter()
router.register(r'project', ProjectReadView)
router.register(r'project_write', ProjectWriteView)
router.register(r'portfolio', PortfolioReadView)
router.register(r'portfolio_write', PortfolioWriteView)
router.register(r'followers', FollowersReadView)

urlpatterns = router.urls
