from django import urls
from rest_framework import routers

from . import views
from . import api


router = routers.DefaultRouter()
router.register(r'raw_flags', api.RawFlagViewSet)


urlpatterns = [
    urls.path('', views.index, name='index'),
    urls.path('my_flags/', views.profile, name='profile'),
    urls.path('graphs/reports_per_day', views.reports_per_day, name='reports_per_day'),
    urls.path('api/v0/', urls.include(router.urls)),
]