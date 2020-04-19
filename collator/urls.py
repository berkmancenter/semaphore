from django import urls
from rest_framework import routers

from . import views
from . import api


router = routers.DefaultRouter()
router.register(r'raw_flags', api.RawFlagViewSet)


urlpatterns = [
    urls.path('', views.index, name='index'),
    urls.path('api/v0/', urls.include(router.urls)),
]