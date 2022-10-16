from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .api import CompanyViewSet, UserViewSet, NoticeViewSet, ApplicationViewSet

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)
router.register('user', UserViewSet)
router.register('notice', NoticeViewSet)
router.register('application', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]