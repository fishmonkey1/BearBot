from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from bear_api import views

urlpatterns = [
    url(r'^user/(?P<account>.+)?$', views.lookup_user),
    url(r'^report/(?P<id>.+)?$', views.lookup_report),
    url(r'^analysis?$', views.generate_report),
]
