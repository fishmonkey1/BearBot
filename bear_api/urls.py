from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from bear_api import views

# router = DefaultRouter()
# router.register(r'questions', views.QuestionsViewSet)

urlpatterns = [
    # url(r'^test/?$', views.Testing.as_view()),
    url(r'^testing/?$', views.Testing.as_view())
]
