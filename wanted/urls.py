from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .api import CompanyViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]