from rest_framework import routers
from .views import ProjectReadView, PortfolioView, ProjectWriteView
from django.conf.urls import url

router = routers.SimpleRouter()
router.register(r'project', ProjectReadView)
router.register(r'portfolio', PortfolioView)
router.register(r'project_write',ProjectWriteView)

urlpatterns = router.urls
