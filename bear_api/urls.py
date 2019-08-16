from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from bear_api import views

# router = DefaultRouter()
# router.register(r'questions', views.QuestionsViewSet)

urlpatterns = [
    url(r'^user/(?P<account>.+)?$', views.Users.as_view()),
    url(r'^reportg/<str:account>?$', views.Users.as_view()),
]
