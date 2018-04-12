from rest_framework import routers
from .views import UserViewset
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'users/get_search_user/(?P<search_user_name>\w+)/', UserViewset)
router.register(r'users/get_search_user/(?P<search_email>\w+)/', UserViewset)

urlpatterns = router.urls