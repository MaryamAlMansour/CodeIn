from rest_framework import routers
from .views import SearchView
from django.conf.urls import url

router = routers.SimpleRouter()
router.register('filter', SearchView)

urlpatterns = router.urls
